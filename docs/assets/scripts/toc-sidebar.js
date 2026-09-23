(() => {
  const page = document.querySelector(".markdown-body");
  if (!page) return;

  const tocHeading = Array.from(page.querySelectorAll("h2")).find(
    (heading) => heading.textContent.trim().toLowerCase() === "table of contents",
  );
  const tocList = tocHeading?.nextElementSibling;
  if (!tocHeading || !tocList || tocList.tagName !== "UL") return;

  const layout = document.createElement("div");
  layout.className = "docs-layout";

  const nav = document.createElement("nav");
  nav.className = "page-toc";
  nav.setAttribute("aria-label", "On this page");

  const details = document.createElement("details");
  const summary = document.createElement("summary");
  summary.textContent = "On this page";
  details.append(summary, tocList);
  nav.append(details);

  const content = document.createElement("main");
  content.className = "docs-content";

  for (const node of Array.from(page.childNodes)) {
    if (node !== tocHeading && node !== tocList) content.append(node);
  }

  layout.append(nav, content);
  page.append(layout);
  page.classList.add("has-page-toc");

  const desktop = window.matchMedia("(min-width: 1001px)");
  const setExpanded = (event) => {
    details.open = event.matches;
  };
  setExpanded(desktop);
  desktop.addEventListener("change", setExpanded);
})();

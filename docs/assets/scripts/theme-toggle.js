(() => {
  const storageKey = "ikemen-docs-theme";
  const root = document.documentElement;
  const systemTheme = window.matchMedia("(prefers-color-scheme: dark)");
  let savedTheme = null;

  try {
    const stored = window.localStorage.getItem(storageKey);
    if (stored === "dark" || stored === "light") savedTheme = stored;
  } catch {
    // Storage can be unavailable in some browser contexts.
  }

  const applyTheme = (theme) => {
    root.dataset.theme = theme;
  };

  applyTheme(savedTheme || (systemTheme.matches ? "dark" : "light"));

  systemTheme.addEventListener("change", (event) => {
    if (!savedTheme) applyTheme(event.matches ? "dark" : "light");
  });

  document.addEventListener("DOMContentLoaded", () => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "theme-toggle";

    const updateButton = () => {
      const isDark = root.dataset.theme === "dark";
      button.textContent = isDark ? "Light theme" : "Dark theme";
      button.setAttribute("aria-label", `Switch to ${isDark ? "light" : "dark"} theme`);
      button.setAttribute("aria-pressed", String(isDark));
    };

    button.addEventListener("click", () => {
      savedTheme = root.dataset.theme === "dark" ? "light" : "dark";
      applyTheme(savedTheme);
      try {
        window.localStorage.setItem(storageKey, savedTheme);
      } catch {
        // Keep the selection for this page even if it cannot be persisted.
      }
      updateButton();
    });

    updateButton();
    document.body.append(button);
  });
})();

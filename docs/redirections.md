# Merged Trigger Redirection Reference

## Table of Contents

- [enemy (M.U.G.E.N)](#enemy-mugen)
- [enemy(n) (M.U.G.E.N)](#enemyn-mugen)
- [enemyNear (M.U.G.E.N)](#enemynear-mugen)
- [enemyNear(n) (M.U.G.E.N)](#enemynearn-mugen)
- [helper (M.U.G.E.N)](#helper-mugen)
- [helper(ID) (M.U.G.E.N)](#helperid-mugen)
- [HelperIndex(n) (new)](#helperindexn-new)
- [P2 (new)](#p2-new)
- [parent (M.U.G.E.N)](#parent-mugen)
- [partner (M.U.G.E.N)](#partner-mugen)
- [partner(n) (M.U.G.E.N)](#partnern-mugen)
- [Player(n) (new)](#playern-new)
- [playerID(ID) (M.U.G.E.N)](#playeridid-mugen)
- [PlayerIndex(n) (nightly build only) (new)](#playerindexn-nightly-build-only-new)
- [root (M.U.G.E.N)](#root-mugen)
- [StateOwner (new)](#stateowner-new)
- [target (M.U.G.E.N)](#target-mugen)
- [target(ID) (M.U.G.E.N)](#targetid-mugen)

---

## enemy (M.U.G.E.N)

*Source: M.U.G.E.N 1.1*

Redirects the trigger to the first opponent found.  
Normal helpers and neutral players are not considered opponents.  
See the related trigger `numenemy` in the trigger documentation.

---

## enemy(n) (M.U.G.E.N)

*Source: M.U.G.E.N 1.1*

`n` should be a well-formed expression that evaluates to a non-negative integer.  
The trigger is redirected to the n'th opponent.

---

## enemyNear (M.U.G.E.N)

*Source: M.U.G.E.N 1.1*

Redirects the trigger to the nearest opponent.

---

## enemyNear(n) (M.U.G.E.N)

*Source: M.U.G.E.N 1.1*

`n` should be a well-formed expression that evaluates to a non-negative integer.  
The trigger is redirected to the n'th-nearest opponent.

---

## helper (M.U.G.E.N)

*Source: M.U.G.E.N 1.1*

Redirects the trigger to the first helper found. See the related  
trigger `NumHelper` in the trigger documentation.

---

## helper(ID) (M.U.G.E.N)

*Source: M.U.G.E.N 1.1*

ID should be a well-formed expression that evaluates to a positive  
integer. The trigger is then redirected to a helper with the  
corresponding ID number.

---

## HelperIndex(n) (new)

*Source: Ikemen GO (new)*

Redirects the trigger to the helper entity by index.

Each helper is assigned an index according to their position among the total number of helpers a player has. These indexes begin at 1, with index 0 being a special case that represents the `root` player. A player with 5 helpers, for instance, will have helpers with indexes 1 through 5.  

```ini
trigger1 = NumHelper >= 2
trigger1 = HelperIndex(2), MoveType = A
```
Nightly build:

In the nightly build, the trigger has been refactored, now it takes redirections into account, allowing the return of a helper's helpers. The old usage still works if the trigger is called from the **Root**. If you need the same result but the call comes from a helper, use: **Root, HelperIndex(1)**.
```ini
trigger1 = HelperIndexExist(2)
trigger1 = HelperIndex(2), MoveType = A
```

---

## P2 (new)

*Source: Ikemen GO (new)*

Redirects the trigger to the same player as the "P2" family of triggers (P2StateNo, etc). So, for instance, `P2, StateNo` is equivalent to `P2StateNo`.  

The "P2" enemy has some notable properties:  
- If it is in state 5150 (KO), it will be ignored  
- Is the one the character will always be facing automatically (`facep2`, etc)  
- Only changes when another enemy is at least 30 pixels closer to the player, making it less erratic during team modes  

All of these properties make `P2` the optimal enemy redirection in most cases.  

Note: This redirection should not be mistaken for "Player(2)", which is always player number 2.  

```ini
trigger1 = P2, DizzyPoints <= 100
```

---

## parent (M.U.G.E.N)

*Source: M.U.G.E.N 1.1*

Redirects the trigger to the player's parent. (Player must be a helper.)

---

## partner (M.U.G.E.N)

*Source: M.U.G.E.N 1.1*

Redirects the trigger to the player's partner. Normal helpers and neutral players are not considered opponents. See the related trigger `numpartner` in the trigger documentation.

---

## partner(n) (M.U.G.E.N)

*Source: M.U.G.E.N 1.1*

`n` should be a well-formed expression that evaluates to a non-negative integer.  
The trigger is redirected to the n'th partner.

---

## Player(n) (new)

*Source: Ikemen GO (new)*

Redirects a trigger to the character with the specified PlayerNo.

```ini
trigger1 = Player(1), AILevel
trigger2 = Player(TeamLeader), MoveType = A
```

---

## playerID(ID) (M.U.G.E.N)

*Source: M.U.G.E.N 1.1*

`n` should be a well-formed expression that evaluates to a non-negative integer.  
The trigger is redirected to the player with unique ID equal to ID. See the `ID` and `PlayerExistID` triggers in the trigger documentation.

---

## PlayerIndex(n) (nightly build only) (new)

*Source: Ikemen GO (new)*

Each player is assigned a specific index in the internal player list. `PlayerIndex` will redirect a trigger to the player (helpers included) with the specified index. The first index is 0. If there are 20 players on screen, valid indexes will be 0 through 19.  
  
Like all "index" triggers, this is especially useful in `for` and `while` loops.  
  
```go
trigger1 = PlayerIndexExist(1)
trigger1 = PlayerIndex(1), id = 56

# Count all explods on screen
let totalExplod = 0;
for i = 0; NumPlayer - 1; 1 {
	if PlayerIndexExist($i) {
		let totalExplod = $totalExplod + PlayerIndex($i), NumExplod;
	}
}
```

---

## root (M.U.G.E.N)

*Source: M.U.G.E.N 1.1*

Redirects the trigger to the root.

---

## StateOwner (new)

*Source: Ikemen GO (new)*

Redirects a trigger to the owner of the current state the character is in. Useful when a custom stated target needs to redirect a trigger to the player.  
Note: states are owned by the root.  

```ini
trigger1 = StateOwner,AILevel
```

---

## target (M.U.G.E.N)

*Source: M.U.G.E.N 1.1*

Redirects the trigger to the first target found.

---

## target(ID) (M.U.G.E.N)

*Source: M.U.G.E.N 1.1*

ID should be a well-formed expression that evaluates to a non-  
negative integer. The trigger is then redirected to a target with  
the corresponding targetID. The targetID is specified in the `ID`  
parameter of a HitDef controller.

---

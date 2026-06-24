# Merged Trigger Redirection Reference

## Table of Contents

- [enemy (old)](#enemy-old)
- [enemy(n) (old)](#enemyn-old)
- [enemyNear (old)](#enemynear-old)
- [enemyNear(n) (old)](#enemynearn-old)
- [helper (old)](#helper-old)
- [Helper (changed)](#helper-changed)
- [helper(ID) (old)](#helperid-old)
- [HelperIndex(n) (new)](#helperindexn-new)
- [P2 (new)](#p2-new)
- [parent (old)](#parent-old)
- [partner (old)](#partner-old)
- [partner(n) (old)](#partnern-old)
- [Player(n) (new)](#playern-new)
- [playerID(ID) (old)](#playeridid-old)
- [PlayerIndex(n) (new)](#playerindexn-new)
- [root (old)](#root-old)
- [StateOwner (new)](#stateowner-new)
- [target (old)](#target-old)
- [Target (changed)](#target-changed)
- [target(ID) (old)](#targetid-old)

---

# Trigger Redirections

## enemy (old)

Redirects the trigger to the first opponent found.  
Normal helpers and neutral players are not considered opponents.  
See the related trigger `numenemy` in the trigger documentation.

---

## enemy(n) (old)

`n` should be a well-formed expression that evaluates to a non-negative integer.  
The trigger is redirected to the n'th opponent.

---

## enemyNear (old)

Redirects the trigger to the nearest opponent.

---

## enemyNear(n) (old)

`n` should be a well-formed expression that evaluates to a non-negative integer.  
The trigger is redirected to the n'th-nearest opponent.

---

## helper (old)

Redirects the trigger to the first helper found. See the related  
trigger `NumHelper` in the trigger documentation.

---

## Helper (changed)

The `Helper` redirection now also accepts an optional index argument, through the new format `Helper(ID, index)`. Defaults to 0 (first one).  
The old formats still work exactly the same.  

Example:
```ini
trigger1 = NumHelper(1005) >= 2
trigger1 = Helper(1005, 1), MoveType = A; The second helper with ID 1005
```

---

## helper(ID) (old)

ID should be a well-formed expression that evaluates to a positive  
integer. The trigger is then redirected to a helper with the  
corresponding ID number.

---

## HelperIndex(n) (new)

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

## parent (old)

Redirects the trigger to the player's parent. (Player must be a helper.)

---

## partner (old)

Redirects the trigger to the player's partner. Normal helpers and neutral players are not considered opponents. See the related trigger `numpartner` in the trigger documentation.

---

## partner(n) (old)

`n` should be a well-formed expression that evaluates to a non-negative integer.  
The trigger is redirected to the n'th partner.

---

## Player(n) (new)

Redirects a trigger to the character with the specified PlayerNo.

```ini
trigger1 = Player(1), AILevel
trigger2 = Player(TeamLeader), MoveType = A
```

---

## playerID(ID) (old)

`n` should be a well-formed expression that evaluates to a non-negative integer.  
The trigger is redirected to the player with unique ID equal to ID. See the `ID` and `PlayerExistID` triggers in the trigger documentation.

---

## PlayerIndex(n) (new)

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

## root (old)

Redirects the trigger to the root.

---

## StateOwner (new)

Redirects a trigger to the owner of the current state the character is in. Useful when a custom stated target needs to redirect a trigger to the player.  
Note: states are owned by the root.  

```ini
trigger1 = StateOwner,AILevel
```

---

## target (old)

Redirects the trigger to the first target found.

---

## Target (changed)

The `Target` redirection now also accepts an optional index argument, through the new format `Target(ID, index)`. Defaults to 0 (first one).  
The old format still works exactly the same.  

Example:
```ini
trigger1 = NumTarget >= 2
trigger1 = Target(-1, 1), Alive; The second target with any ID
```

---

## target(ID) (old)

ID should be a well-formed expression that evaluates to a non-  
negative integer. The trigger is then redirected to a target with  
the corresponding targetID. The targetID is specified in the `ID`  
parameter of a HitDef controller.

---

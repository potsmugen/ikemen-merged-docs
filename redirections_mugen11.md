## parent  
Redirects the trigger to the player's parent. (Player must be a helper.)  
  
## root  
Redirects the trigger to the root.  
  
## helper  
Redirects the trigger to the first helper found. See the related  
trigger `NumHelper` in the trigger documentation.  
  
## helper(ID)  
ID should be a well-formed expression that evaluates to a positive  
integer. The trigger is then redirected to a helper with the  
corresponding ID number.  
  
## target  
Redirects the trigger to the first target found.  
  
## target(ID)  
ID should be a well-formed expression that evaluates to a non-  
negative integer. The trigger is then redirected to a target with  
the corresponding targetID. The targetID is specified in the `ID`  
parameter of a HitDef controller.  
  
## partner  
Redirects the trigger to the player's partner. Normal helpers and neutral players are not considered opponents. See the related trigger `numpartner` in the trigger documentation.  
  
## partner(n)  
`n` should be a well-formed expression that evaluates to a non-negative integer.  
The trigger is redirected to the n'th partner.  
  
## enemy  
Redirects the trigger to the first opponent found.  
Normal helpers and neutral players are not considered opponents.  
See the related trigger `numenemy` in the trigger documentation.  
  
## enemy(n)  
`n` should be a well-formed expression that evaluates to a non-negative integer.  
The trigger is redirected to the n'th opponent.  
  
## enemyNear  
Redirects the trigger to the nearest opponent.  
  
## enemyNear(n)  
`n` should be a well-formed expression that evaluates to a non-negative integer.  
The trigger is redirected to the n'th-nearest opponent.  
  
## playerID(ID)  
`n` should be a well-formed expression that evaluates to a non-negative integer.  
The trigger is redirected to the player with unique ID equal to ID. See the `ID` and `PlayerExistID` triggers in the trigger documentation.  
  
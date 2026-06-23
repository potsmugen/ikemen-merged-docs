# Merged Trigger Reference

## Table of Contents

- [Abs (math) (old)](#abs-math-old)
- [Acos (math) (old)](#acos-math-old)
- [AILevel (old)](#ailevel-old)
- [AiLevelF (new)](#ailevelf-new)
- [AirJumpCount (new)](#airjumpcount-new)
- [Alive (old)](#alive-old)
- [Alpha (new)](#alpha-new)
- [Analog (new)](#analog-new)
- [Angle (new)](#angle-new)
- [Anim (old)](#anim-old)
- [AnimElem (old)](#animelem-old)
- [AnimElemNo (old)](#animelemno-old)
- [AnimElemTime (old)](#animelemtime-old)
- [AnimElemVar (new)](#animelemvar-new)
- [AnimExist (old)](#animexist-old)
- [AnimLength (new)](#animlength-new)
- [AnimPlayerNo (new)](#animplayerno-new)
- [AnimTime (old)](#animtime-old)
- [Asin (math) (old)](#asin-math-old)
- [Atan (math) (old)](#atan-math-old)
- [Atan2 (Math) (new)](#atan2-math-new)
- [Attack (new)](#attack-new)
- [AttackMul (new)](#attackmul-new)
- [AuthorName (old)](#authorname-old)
- [BackEdge (old)](#backedge-old)
- [BackEdgeBodyDist (old)](#backedgebodydist-old)
- [BackEdgeDist (old)](#backedgedist-old)
- [BgmVar (new)](#bgmvar-new)
- [BotBoundBodyDist (new)](#botboundbodydist-new)
- [BotBoundDist (new)](#botbounddist-new)
- [BottomEdge (old)](#bottomedge-old)
- [CameraPos (old)](#camerapos-old)
- [CameraZoom (old)](#camerazoom-old)
- [CanRecover (old)](#canrecover-old)
- [Ceil (math) (old)](#ceil-math-old)
- [Clamp (Math) (new)](#clamp-math-new)
- [ClsnOverlap (new)](#clsnoverlap-new)
- [ClsnVar (new)](#clsnvar-new)
- [ComboCount (new)](#combocount-new)
- [Command (old)](#command-old)
- [Command (changed)](#command-changed)
- [Cond (math) (old)](#cond-math-old)
- [ConsecutiveWins (new)](#consecutivewins-new)
- [Const (old)](#const-old)
- [Const (changed)](#const-changed)
- [Const1080p (new)](#const1080p-new)
- [Const240p (old)](#const240p-old)
- [Const480p (old)](#const480p-old)
- [Const720p (old)](#const720p-old)
- [Cos (math) (old)](#cos-math-old)
- [Ctrl (old)](#ctrl-old)
- [DebugMode (new)](#debugmode-new)
- [DecisiveRound (new)](#decisiveround-new)
- [Defence (new)](#defence-new)
- [DefenceMul (new)](#defencemul-new)
- [Deg (Math) (new)](#deg-math-new)
- [DisplayName (new)](#displayname-new)
- [Dizzy (new)](#dizzy-new)
- [DizzyPoints (new)](#dizzypoints-new)
- [DizzyPointsMax (new)](#dizzypointsmax-new)
- [DrawGame (old)](#drawgame-old)
- [DrawPal (new)](#drawpal-new)
- [E (math) (old)](#e-math-old)
- [EnvShakeVar (new)](#envshakevar-new)
- [Exp (math) (old)](#exp-math-old)
- [ExplodVar (new)](#explodvar-new)
- [Facing (old)](#facing-old)
- [FightScreenState (new)](#fightscreenstate-new)
- [FightScreenVar (new)](#fightscreenvar-new)
- [FightTime (new)](#fighttime-new)
- [FirstAttack (new)](#firstattack-new)
- [Float (math) (new)](#float-math-new)
- [Floor (math) (old)](#floor-math-old)
- [FrontEdge (old)](#frontedge-old)
- [FrontEdgeBodyDist (old)](#frontedgebodydist-old)
- [FrontEdgeDist (old)](#frontedgedist-old)
- [FVar (old)](#fvar-old)
- [GameHeight (old)](#gameheight-old)
- [GameHeight (changed)](#gameheight-changed)
- [GameMode (new)](#gamemode-new)
- [GameOption (new)](#gameoption-new)
- [GameTime (old)](#gametime-old)
- [GameVar (new)](#gamevar-new)
- [GameWidth (old)](#gamewidth-old)
- [GameWidth (changed)](#gamewidth-changed)
- [GetHitVar (old)](#gethitvar-old)
- [GetHitVar (changed)](#gethitvar-changed)
- [GroundAngle (new)](#groundangle-new)
- [GroundLevel (new)](#groundlevel-new)
- [GuardBreak (new)](#guardbreak-new)
- [GuardCount (new)](#guardcount-new)
- [GuardPoints (new)](#guardpoints-new)
- [GuardPointsMax (new)](#guardpointsmax-new)
- [HelperIndexExist(n) (new)](#helperindexexistn-new)
- [HelperName (new)](#helpername-new)
- [HelperVar (new)](#helpervar-new)
- [HitByAttr (new)](#hitbyattr-new)
- [HitCount (old)](#hitcount-old)
- [HitDefAttr (old)](#hitdefattr-old)
- [HitDefVar (new)](#hitdefvar-new)
- [HitFall (old)](#hitfall-old)
- [HitOver (old)](#hitover-old)
- [HitOverridden (new)](#hitoverridden-new)
- [HitPauseTime (old)](#hitpausetime-old)
- [HitShakeOver (old)](#hitshakeover-old)
- [HitVel (old)](#hitvel-old)
- [ID (old)](#id-old)
- [IfElse (math) (old)](#ifelse-math-old)
- [IkemenVersion (new)](#ikemenversion-new)
- [InCustomAnim (new)](#incustomanim-new)
- [InCustomState (new)](#incustomstate-new)
- [Index (new)](#index-new)
- [InDialogue (new)](#indialogue-new)
- [InGuardDist (old)](#inguarddist-old)
- [InputTime (new)](#inputtime-new)
- [IntroState (new)](#introstate-new)
- [IsAsserted (new)](#isasserted-new)
- [IsClsnProxy (new)](#isclsnproxy-new)
- [IsHelper (old)](#ishelper-old)
- [IsHelper (changed)](#ishelper-changed)
- [IsHomeTeam (old)](#ishometeam-old)
- [IsHost (new)](#ishost-new)
- [JugglePoints (new)](#jugglepoints-new)
- [LastPlayerID (new)](#lastplayerid-new)
- [LayerNo (new)](#layerno-new)
- [LeftEdge (old)](#leftedge-old)
- [Lerp (Math) (new)](#lerp-math-new)
- [Life (old)](#life-old)
- [LifeMax (old)](#lifemax-old)
- [Ln (math) (old)](#ln-math-old)
- [LocalCoord (new)](#localcoord-new)
- [Log (math) (old)](#log-math-old)
- [Lose (old)](#lose-old)
- [Map (new)](#map-new)
- [MatchNo (old)](#matchno-old)
- [MatchOver (old)](#matchover-old)
- [Max (math) (new)](#max-math-new)
- [MemberNo (new)](#memberno-new)
- [Min (math) (new)](#min-math-new)
- [MotifState (new)](#motifstate-new)
- [MotifVar (new)](#motifvar-new)
- [MoveContact (old)](#movecontact-old)
- [MoveCountered (new)](#movecountered-new)
- [MoveGuarded (old)](#moveguarded-old)
- [MoveHit (old)](#movehit-old)
- [MoveHitVar (new)](#movehitvar-new)
- [MoveReversed (old)](#movereversed-old)
- [MoveType (old)](#movetype-old)
- [MugenVersion (new)](#mugenversion-new)
- [Name (old)](#name-old)
- [New (new)](#new-new)
- [NumEnemy (old)](#numenemy-old)
- [NumExplod (old)](#numexplod-old)
- [NumHelper (old)](#numhelper-old)
- [NumPartner (old)](#numpartner-old)
- [NumPlayer (new)](#numplayer-new)
- [NumProj (old)](#numproj-old)
- [NumProjID (old)](#numprojid-old)
- [NumStageBG (new)](#numstagebg-new)
- [NumTarget (old)](#numtarget-old)
- [NumText (new)](#numtext-new)
- [Offset (new)](#offset-new)
- [OutroState (new)](#outrostate-new)
- [P1Name (old)](#p1name-old)
- [P2BodyDist (old)](#p2bodydist-old)
- [P2BodyDist (changed)](#p2bodydist-changed)
- [P2Dist (old)](#p2dist-old)
- [P2Dist Z (changed)](#p2dist-z-changed)
- [P2Life (old)](#p2life-old)
- [P2MoveType (old)](#p2movetype-old)
- [P2Name (old)](#p2name-old)
- [P2StateNo (old)](#p2stateno-old)
- [P2StateType (old)](#p2statetype-old)
- [P3Name (old)](#p3name-old)
- [P4Name (old)](#p4name-old)
- [P5Name, P6Name, P7Name, P8Name (new)](#p5name-p6name-p7name-p8name-new)
- [PalFXVar (new)](#palfxvar-new)
- [PalNo (old)](#palno-old)
- [ParentDist (old)](#parentdist-old)
- [ParentDist Z (changed)](#parentdist-z-changed)
- [ParentExist (new)](#parentexist-new)
- [PauseTime (new)](#pausetime-new)
- [Physics (new)](#physics-new)
- [Pi (math) (old)](#pi-math-old)
- [PlayerIDExist (old)](#playeridexist-old)
- [PlayerIndexExist(n) (new)](#playerindexexistn-new)
- [PlayerNo (new)](#playerno-new)
- [PlayerNoExist (new)](#playernoexist-new)
- [Pos (old)](#pos-old)
- [Power (old)](#power-old)
- [PowerMax (old)](#powermax-old)
- [PrevAnim (new)](#prevanim-new)
- [PrevMoveType (new)](#prevmovetype-new)
- [PrevStateNo (old)](#prevstateno-old)
- [PrevStateType (new)](#prevstatetype-new)
- [ProjCancelTime (old)](#projcanceltime-old)
- [ProjClsnOverlap (new)](#projclsnoverlap-new)
- [ProjContact (old)](#projcontact-old)
- [ProjContactTime (old)](#projcontacttime-old)
- [ProjGuarded (old)](#projguarded-old)
- [ProjGuardedTime (old)](#projguardedtime-old)
- [ProjHit (old)](#projhit-old)
- [ProjHitTime (old)](#projhittime-old)
- [ProjVar (new)](#projvar-new)
- [Rad (Math) (new)](#rad-math-new)
- [Random (old)](#random-old)
- [RandomRange(math) (new)](#randomrangemath-new)
- [ReceivedDamage (new)](#receiveddamage-new)
- [ReceivedHits (new)](#receivedhits-new)
- [RedLife (new)](#redlife-new)
- [ReversalDefAttr (new)](#reversaldefattr-new)
- [RightEdge (old)](#rightedge-old)
- [RootDist (old)](#rootdist-old)
- [RootDist Z (changed)](#rootdist-z-changed)
- [Round (math) (new)](#round-math-new)
- [RoundNo (old)](#roundno-old)
- [RoundsExisted (old)](#roundsexisted-old)
- [RoundState (old)](#roundstate-old)
- [RoundState (changed)](#roundstate-changed)
- [RoundsWon (new)](#roundswon-new)
- [RoundTime (new)](#roundtime-new)
- [RunOrder (new)](#runorder-new)
- [Scale (new)](#scale-new)
- [Score (new)](#score-new)
- [ScoreTotal (new)](#scoretotal-new)
- [ScreenHeight (old)](#screenheight-old)
- [ScreenPos (old)](#screenpos-old)
- [ScreenWidth (old)](#screenwidth-old)
- [SelfAnimExist (old)](#selfanimexist-old)
- [SelfCommand (new)](#selfcommand-new)
- [SelfStatenoExist (new)](#selfstatenoexist-new)
- [Sign (Math) (new)](#sign-math-new)
- [Sin (math) (old)](#sin-math-old)
- [SoundVar (new)](#soundvar-new)
- [SpriteVar (new)](#spritevar-new)
- [SprPriority (new)](#sprpriority-new)
- [StageBackEdgeDist (new)](#stagebackedgedist-new)
- [StageBGVar (new)](#stagebgvar-new)
- [StageConst (new)](#stageconst-new)
- [StageFrontEdgeDist (new)](#stagefrontedgedist-new)
- [StageTime (new)](#stagetime-new)
- [StageVar (old)](#stagevar-old)
- [StageVar (changed)](#stagevar-changed)
- [Standby (new)](#standby-new)
- [StateNo (old)](#stateno-old)
- [StateType (old)](#statetype-old)
- [SysFVar (old)](#sysfvar-old)
- [SysVar (old)](#sysvar-old)
- [Tan (math) (old)](#tan-math-old)
- [TeamLeader (new)](#teamleader-new)
- [TeamMode (old)](#teammode-old)
- [TeamMode = Tag (changed)](#teammode-tag-changed)
- [TeamSide (old)](#teamside-old)
- [TeamSize (new)](#teamsize-new)
- [TicksPerSecond (old)](#tickspersecond-old)
- [Time (old)](#time-old)
- [TimeElapsed (new)](#timeelapsed-new)
- [TimeMod (old)](#timemod-old)
- [TimeRemaining (new)](#timeremaining-new)
- [TimeTotal (new)](#timetotal-new)
- [TopBoundBodyDist (new)](#topboundbodydist-new)
- [TopBoundDist (new)](#topbounddist-new)
- [TopEdge (old)](#topedge-old)
- [UniqHitCount (old)](#uniqhitcount-old)
- [Var (old)](#var-old)
- [Vel (old)](#vel-old)
- [Win (old)](#win-old)
- [WinClutch (new)](#winclutch-new)
- [WinHyper (new)](#winhyper-new)
- [WinSpecial (new)](#winspecial-new)
- [XAngle (new)](#xangle-new)
- [Xshear (new)](#xshear-new)
- [YAngle (new)](#yangle-new)
- [ZoomVar (new)](#zoomvar-new)

---

# State Controller Reference

## Abs (math) (old)

Computes the absolute value of its argument.  
  
**Format:**  
abs(exprn)  
  
**Arguments:**  

**exprn**  
Expression to compute the absolute value of.
  
  
**Return type:**  
Same as the type of exprn.  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom.

---

## Acos (math) (old)

Computes the arccosine (in radians) of the specified argument.  
  
**Format:**  
acos(exprn)  
  
**Arguments:**  

**exprn**  
Expression to compute the arccosine of (float).
  
  
**Return type:**  
float  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom, or if exprn is not in  
the domain of arccosine (which is `[-1.0,1.0]`).  
  
Example:  
```  
value = acos(1)  
  Sets value to the arccosine of 1, which is approximately 0.0  
  (possibly with some rounding error.)  
```

---

## AILevel (old)

Returns the difficulty level of the player's AI.  
  
**Format:**  
AILevel  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
**Details:**  
If AI is enabled on the player, the value ranges from 1 (easiest) to 8 (most difficult).  
If AI is not enabled on the player, the return value is 0.  
  
Example:  
```  
trigger1 = Random < AILevel * 10  
; Triggers with 10% probability at AILevel 1, 20% at AILevel 2, etc.  
```

---

## AiLevelF (new)

Returns the difficulty level of the player's AI as float value (unlike *AILevel* trigger, which is still floored for compatibility reasons). If AI is enabled on the player, the value ranges from 1 (easiest) to 8 (most difficult). If AI is not enabled on the player, the return value is 0. AI difficulty level with floating point is a result of AI Ramping system (refer to select.def distributed with engine for more information)

>Format:  
>AILevelF  
>  
>Arguments:  
>none  
>  
>Return type:  
>float  

```ini
trigger1 = Random < (500 * (AILevelF ** 2 / 64.0))
```

---

## AirJumpCount (new)

Returns the number of (conventional) air jumps the P1 has performed.

>Format:  
>AirJumpCount  
>  
>Arguments:  
>none  
>  
>Return type:  
>int

---

## Alive (old)

Returns 1 if the player is still able to fight, 0 if the player has been KOed.  
  
**Format:**  
alive  
  
**Arguments:**  
none  
  
**Return type:**  
boolean int (1 or 0)  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = Alive = 0  
; Triggers if the player has been KOed.  
```

---

## Alpha (new)

Returns the value of the player's source/dest alpha applied with Trans sctrl.

>Format:  
>Alpha argument
>  
>Arguments:  
>source, dest
>  
>Return type:
>int

```ini
trigger1 = Alpha source >= 128 && Alpha dest >= 128
```

---

## Analog (new)

Returns the value of the player's respective analog axis. Values are normalized from [-1,1] with the exception of analog triggers (`RightTrigger` and `LeftTrigger`) which are normalized to [0.0,1.0].

Note: internally, 256 distinct analog steps exist per axis with the exception of the analog triggers which are halved (128 distinct steps).

>Format:  
>Axis argument
>  
>Arguments:  
>LeftX, LeftY, RightX, RightY, LeftTrigger, RightTrigger
>  
>Return type:
>float

```ini
trigger1 = Analog(LeftX) >= 0.5 && Analog(RightTrigger) > 0.75
```

---

## Angle (new)

Returns the value of the player's angle applied with AngleDraw/AngleSet/AngleAdd/AngleMul sctrl.

>Format:  
>Angle
>  
>Arguments:  
>none  
>  
>Return type:
>float

```ini
trigger1 = Angle >= 90
```

---

## Anim (old)

Returns the current animation action number of the player.  
  
**Format:**  
Anim  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = Anim = 200  
; Triggers if the player is currently in action 200.  
```

---

## AnimElem (old)

Gets the animation-time elapsed since the start of a specified element of the current animation action. Useful for synchronizing events to elements of an animation action.  
(reminder: first element of an action is element 1, not 0)  
AnimElemTime has similar functionality to AnimElem, but can take expressions as its argument.  
  
**Format:**  
- AnimElem = value1  
- AnimElem = value1, [oper] value2  
  
**Arguments:**  

*[oper]*  
=, !=, <, >, <=, >=  
*value1 (int)*  
Element number to check.  
*value2 (int)*  
Value of animation-time to compare with.
  
  
**Return type:**  
boolean int (1 or 0)  
  
**Error conditions:**  
Returns bottom if the specified element number is invalid for this  
action (e.g., it's too large or too small).  
  
**Details:**  
Trigger in Format 1 is true if the player's animation is at the start of the element number specified by value1.  
In other words, if value1 is equal to n, it is true on the first game-tick of the nth element of the animation.  
Trigger in Format 2 compares the player's animation-time to `t+value2`, where `t` is time of the start of the element number specified by `value1`.  
  
  
**Notes:**  
AnimElem will not trigger on the first game-tick of the second or later loop of an animation with a finite looptime.  
For example, "AnimElem = 1" will trigger the first tick a player changes to an animation, but will not trigger on the tick that it loops. You may get it to trigger each time using `AnimElem = 1 || AnimTime = 0`.  
  
Examples:  
```  
trigger1 = AnimElem = 2  
; True on the first game-tick that the player's animation is on element 2.
; Is equivalent to saying: trigger1 = AnimElem = 2, = 0  
  
trigger1 = AnimElem = 2, = 4  
; True 4 game-ticks after the start of the player's second animation element.  
  
trigger1 = AnimElem = 2, >= 0  
trigger1 = AnimElem = 3, < 0  
; True for the whole of the second element of the player's animation, assuming there is a third element.
; If a third element does not exist, the second line should read, trigger1 = AnimTime <= 0  
```

---

## AnimElemNo (old)

Returns the number of the animation element in the current action  
that would be displayed at the specified time. The argument to AnimElemNo represents the time to check, expressed in game ticks, relative to the present.  
  
**Format:**  
AnimElemNo(exprn)  
  
**Arguments:**  

**exprn**  
Expression that evaluates to the time offset (int).
  
  
**Return type:**  
int  
  
**Error conditions:**  
Returns bottom if you try to check a time that would fall before the  
start of the current action.  
  
**Notes:**  
If the action is currently within its looping portion, then it is  
assumed to have been looping forever. That is, no matter how far into  
the past you check, AnimElemNo will always return an element number  
that lies within the looping portion of the action.  
  
Examples:  
```  
trigger1 = AnimElemNo(0) = 2  
; True when the animation element to be displayed 0 ticks in the  
  future (i.e., now) is element 2. This is equivalent to:  
  trigger1 = AnimElem = 2, >= 0  
  trigger1 = AnimElem = 3, < 0  
  
trigger1 = AnimElemNo(2) = 4  
; True when the animation element that will be displayed two ticks  
  from now is element 4. This is equivalent to:  
  trigger1 = AnimElem = 4, >= -2  
  trigger1 = AnimElem = 5, < -2  
```

---

## AnimElemTime (old)

Gets the animation-time elapsed since the start of a specified element of the current animation action. Useful for synchronizing events to elements of an animation action.  
(reminder: first element of an action is element 1, not 0)  
  
**Format:**  
AnimElemTime(exprn)  
  
**Arguments:**  

**exprn**  
Expression that evaluates to the element number to check (int).
  
  
**Return type:**  
int  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom, or if exprn evaluates  
to an element number that is not valid for the current action.  
  
**Notes:**  
AnimElemTime will not trigger on the first game-tick of the second or later loop of an animation with a finite looptime. For example, "AnimElemTime(1) = 0" will trigger the first tick a player changes to an animation, but will not trigger on the tick that it loops. You may get it to trigger each time using "AnimElemTime(1) = 0 || AnimTime = 0".  
  
Examples:  
```  
trigger1 = AnimElemTime(2) = 0  
  True on the first game-tick that the player's animation  
  is on element 2. Is equivalent to saying:  
  trigger1 = AnimElem = 2  
  
trigger1 = AnimElemTime(2) = 4  
  True 4 game-ticks after the start of the player's  
  second animation element.  
  
trigger1 = AnimElemTime(2) >= 0  
trigger1 = AnimElemTime(3) < 0  
  True for the whole of the second element of the player's  
  animation, assuming there is a third element. If a  
  third element does not exist, the second line will evaluate  
  to bottom and hence trigger1 will never trigger. In this case,  
  the second line should read,  
  trigger1 = AnimTime <= 0  
```

---

## AnimElemVar (new)

Returns information about the player's current animation frame as defined in the AIR file. Refer to the AIR file documentation for what each parameter means.  
Note: This trigger was also called `AnimFrame` at one point during development.  

>Format:  
>AnimElemVar(param_name)  
>  
>Arguments:  
>param_name  
>The name of the parameter to check. Valid values are:  
>AlphaDest, AlphaSource, Angle, Group, HFlip, Image, NumClsn1, NumClsn2, Time, VFlip, XOffset, XScale, YOffset, YScale  

```ini
trigger1 = AnimElemVar(Group) = 200
trigger1 = AnimElemVar(NumClsn1) > 0
```

---

## AnimExist (old)

Returns 1 if the specified animation action exists for the player.  
The result of this trigger is undefined if the player has been placed in a custom state by a successful hit. In this situation, use SelfAnimExist.  
  
**Format:**  
AnimExist(exprn)  
  
**Arguments:**  

**exprn**  
An expression evaluating to an animation number (int).
  
  
**Return type:**  
boolean int (1 or 0)  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom.  
  
Example:  
```  
trigger1 = !AnimExist(200)  
; Triggers if the player is missing action 200.  
```

---

## AnimLength (new)

Returns total length of the P1 current animation.

>Format:  
>AnimLength  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = Time = AnimTime - AnimLength
trigger1 = Time = GetHitVar(hittime) - AnimLength
```

---

## AnimPlayerNo (new)

Returns the player number of the owner of the player's current animation.  
Normally returns the same number as the player's player number, but when for instance `ChangeAnim2` is used in a custom state, it will return the number of who owns that animation.  

>Format:  
>AnimPlayerNo  
>  
>Arguments:  
>none  
>  
>Return type:  
>int

```ini
trigger1 = Player(AnimPlayerNo), SelfAnimExist(1234)
```

---

## AnimTime (old)

Gives the difference between the looptime of the current animation action and the player's animation-time. Useful for knowing when the end of the animation has been reached. (Animation-time is the time in game-ticks that the player has spent within the current animation action.)  
The name may be confusing. Try to think of it as "time from the end of the animation". During the animation, AnimTime will always return a non-positive number.  
  
**Format:**  
AnimTime  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = AnimTime = 0  
; Triggers when the animation-time is equal to the animation  
  action's looptime, ie. the end of the action has been  
  reached.  
```

---

## Asin (math) (old)

Computes the arcsine (in radians) of the specified argument.  
  
**Format:**  
asin(exprn)  
  
**Arguments:**  

**exprn**  
Expression to compute the arcsine of (float).
  
  
**Return type:**  
float  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom, or if exprn is not in  
the domain of arcsine (which is `[-1.0,1.0]`).  
  
Example:  
```  
value = asin(1)  
  Sets value to the arcsine of 1, which is approximately pi/2  
  (possibly with some rounding error.)  
```

---

## Atan (math) (old)

Computes the arctangent (in radians) of the specified argument.  
  
**Format:**  
atan(exprn)  
  
**Arguments:**  

**exprn**  
Expression to compute the arctangent of (float).
  
  
**Return type:**  
float  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom.  
  
Example:  
```  
value = atan(1)  
  Sets value to the arccosine of 1, which is approximately pi/4  
  (possibly with some rounding error.)  
```

---

## Atan2 (Math) (new)

Takes two arguments, and returns the arc tangent of the two specified arguments.

>Format:  
>Atan2(exp1,exp2)  
>  
>Arguments:  
>exp1  
>Expression 1  
>  
>exp2  
>Expression 2  
>  
>Return type:  
>float  

```ini
fvar(10) = Atan2(enemy,pos y-pos y, enemy,pos x-pos x)
```

---

## Attack (new)

Returns P1 current attack value.

>Format:  
>Attack  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = Attack = 100
```

---

## AttackMul (new)

Returns the player's current attackmul value.

>Format:  
>AttackMul  
>  
>Arguments:  
>none  
>  
>Return type:  
>float  

```ini
trigger1 = AttackMul > 1.0
```

---

## AuthorName (old)

Returns the player's author's name (specified in the .DEF file). This may also be useful for telling apart characters with the same name but different authors.  
  
**Format:**  
AuthorName [oper] "name"  
  
**Arguments:**  

**[oper]**  
=, != (other operators not valid)  
**"name" (string)**  
Name to compare against. Must be in double quotes.
  
  
**Return type:**  
boolean int (1 or 0)  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = Authorname = "Suika"  
  Returns true if the character's author is named Suika.  
```

---

## BackEdge (old)

BackEdge returns the x position of the edge of the screen that is behind the player, in absolute stage coordinates.  
  
**Format:**  
BackEdge  
  
**Arguments:**  
none  
  
**Return type:**  
float  
  
**Error conditions:**  
none  
  
**Notes:**  
This trigger is equivalent to the expression "ifelse(facing = 1, LeftEdge, RightEdge)".  
  
Example:  
```  
trigger1 = Pos X + CameraPos X < BackEdge  
; Triggers if the player is to the left of the back edge of the screen.  
```

---

## BackEdgeBodyDist (old)

BackEdgeBodyDist gives the distance from the back of the player, as determined by the end of his width bar, to the back edge of the screen.  
  
**Format:**  
BackEdgeBodyDist  
  
**Arguments:**  
none  
  
**Return type:**  
float  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = BackEdgeBodyDist < 30  
; Triggers if the back of the player’s width bar is within 30 pixels  
  of the edge of the screen in back of him.  
```

---

## BackEdgeDist (old)

BackEdgeDist gives the distance between the x-axis of the player and the edge of the screen behind of the player.  
  
**Format:**  
BackEdgeDist  
  
**Arguments:**  
none  
  
**Return type:**  
float  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = BackEdgeDist < 30  
; Triggers if the x-axis of the player is within 30 pixels of the edge of the screen in back of him.  
```

---

## BgmVar (new)

Allows checking the filename, freqmul, length, loop, loopcount, loopend, loopstart, position, startposition, and volume of the currently playing BGM.

**Warning: The results of this trigger are NOT network-safe due to user settings such as `Sound.BGMRAMSwap` causing variability in the asynchronicity of BGM operations. Usage of this trigger in production environments is discouraged.**

>Format:  
>BGMVar  
>  
>Arguments:  
>param_name  
>The name of the variable to check. Valid values are:  
>filename, freqmul, length, loop, loopcount, loopend, loopstart, position, startposition, volume.  
>  
>Return type:  
>variable

```ini
trigger1 = BGMVar(position) = 32768
trigger2 = BGMVar(startPosition) = 0
trigger3 = BGMVar(loopstart) = 1741
trigger4 = BGMVar(loopend) = 65536
trigger5 = BGMVar(volume) = 98
trigger6 = BGMVar(filename) = "sound/test.mp3"
trigger7 = BGMVar(length) = 65536
```

---

## BotBoundBodyDist (new)

Like `BotBoundDist`, except this trigger accounts for the player's bottom `edge` parameter, as defined by the `Depth` state controller.

---

## BotBoundDist (new)

BotBoundDist gives the distance between the player's z-axis and the `botbound` limit of the stage.

>Format:  
>BotBoundDist 
>  
>Arguments:  
>none  
>  
>Return type:  
>float

```ini
trigger1 = BotBoundDist < 40
```

---

## BottomEdge (old)

BottomEdge returns the y position of the bottom edge of the screen, in absolute stage coordinates.  
  
**Format:**  
BottomEdge  
  
**Arguments:**  
none  
  
**Return type:**  
float  
  
**Error conditions:**  
none  
  
**Notes:**  
This trigger is equivalent to the expression "Pos Y - ScreenPos Y + GameHeight".  
  
Example:  
```  
trigger1 = Pos Y < BottomEdge  
; Triggers if the player is above the bottom edge of the screen.  
```

---

## CameraPos (old)

Gets the value of the camera's position relative to the stage.  
  
**Format:**  
CameraPos [component]  
  
**Arguments:**  

**[component]**  
X, Y
  
  
**Return type:**  
float  
  
**Error conditions:**  
none  
  
**Details:**  
The home position of the camera is 0, 0.  
The value of "CameraPos X" increases as the camera moves to the right.  
The value of "CameraPos Y" decreases as the camera moves upwards.  
The units of the position returned is in the coordspace of the player.  
  
  
Example:  
```  
; True when the camera is to the left of the center of the stage.  
```

---

## CameraZoom (old)

Gets the value of the camera's zoom factor.  
  
**Format:**  
CameraZoom  
  
**Arguments:**  
none  
  
**Return type:**  
float  
  
**Error conditions:**  
none  
  
**Details:**  
The zoom factor de  
  
Example:  
```  
fvar(1) = CameraZoom * ScreenWidth  
; Sets fvar(1) to the distance between the left and right edges of the screen.
; The expression "CameraZoom * ScreenWidth" is equivalent to the GameWidth trigger.  
```

---

## CanRecover (old)

If the player is currently in a falling state, returns 1 if he is currently able to recover, and 0 if he is not currently able to recover. If the player is not currently falling, the output of this trigger is undefined.  
  
**Format:**  
CanRecover  
  
**Arguments:**  
none  
  
**Return type:**  
boolean int (1 or 0)  
  
**Error conditions:**  
none

---

## Ceil (math) (old)

Implements the "ceiling" function. Returns the least integer which is greater than or equal to the specified argument.  
  
**Format:**  
ceil(exprn)  
  
**Arguments:**  

**exprn**  
Expression to compute the ceil of.
  
  
**Return type:**  
int  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom.  
  
Example:  
```  
value = ceil(5.5)  
; Sets value to 6.  
  
value = ceil(-2)  
; Sets value to -2.  
```

---

## Clamp (Math) (new)

Takes three arguments, returns a value clamped to an inclusive range of two specified arguments.
>Format:  
>Clamp(value,min,max)  
>  
>Arguments:  
>value  
>Expression 1  
>  
>min  
>Expression 2  
>  
>max  
>Expression 3  
>  
>Return type:  
>float  

```ini
fvar(10) = Clamp(fvar(10),10 100)
```

---

## ClsnOverlap (new)

Returns true if the player's specified collision box type is overlapping another player's collision boxes.  
This trigger uses Ikemen's internal collision detection, so it will work even with angled and rescaled boxes.  

>Format:  
>ClsnOverlap(box_type_1, playerID, box_type_2)  
>  
>Arguments:  
>box_type_1  
>The player's collision box type. Valid values are clsn1, clsn2, and size  
>  
>playerID  
>The ID of the player against which to check the overlap  
>  
>box_type_2  
>The target's collision box type. Valid values are clsn1, clsn2, and size  
>  
>Return type:  
>boolean int (1 or 0)  

```ini
trigger1 = ClsnOverlap(clsn1, p2,ID, clsn2)
```

---

## ClsnVar (new)

Returns the specified CLSN coordinate from the specified CLSN index. Back always returns the back coordinate, and front always returns the front coordinate, even if they are reversed in the .AIR file. All coordinates are in the same coordinate space as .AIR.
>Format:  
>ClsnVar(value_type,index,elem)  
>  
>Arguments:  
>value_type  
>Valid Values are clsn1, clsn2, and size  
>  
>index  
>Expression  
>  
>elem  
>Valid values are back, front, top, and bottom  
>  
>Return type:  
>float  

```ini
fvar(0) = ClsnVar(Clsn2, 0, Back)
```

---

## ComboCount (new)

Returns the total number of hits done by the player's side in the currently ongoing combo. This value is valid as long as the opposite team combo count stays above 0, otherwise it returns 0 too. Returned value always matches current combo counter tracked by lifebar.

>Format:  
>ComboCount  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = ComboCount > 8
```

---

## Command (old)

Triggers if the user has input the specified command.  
  
**Format:**  
Command [oper] "command_name"  
  
**Arguments:**  

**[oper]**  
=, != (other operators not valid)  
**"command_name" (string)**  
Name of the command. Commands are defined in the  
player's CMD file, and are case-sensitive.  
If the CMD has multiple commands with the same name,  
then any one of those commands will work. Command names  
must appear within double quotes.
  
  
**Return type:**  
boolean int (1 or 0)  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = Command = "fireball motion"  
; True if the user inputs the command corresponding to the command name "fireball motion".  
```

---

## Command (changed)

If a character has `ikemenversion`, when the `Command` trigger is redirected to another player, the engine will first check if the other player is performing its own command with the same name. If not, it'll check if it's performing the command from our own command list. Otherwise it will work like Mugen.

---

## Cond (math) (old)

This trigger takes three arguments.  
The first argument is a condition argument. If the condition is true (i.e., nonzero), Cond evaluates and returns the second argument. If the condition is false, Cond evaluates and returns the third argument. If the condition is bottom, then Cond returns bottom without evaluating the second or third arguments.  
In all cases, any unused argument(s) are not evaluated. Therefore, Cond can be used instead of IfElse to avoid any side effects that would be caused by evaluating the unused argument (e.g., variable assignment, or performing a computation that would cause bottom to be generated).  
  
**Format:**  
Cond(exp_cond,exp_true,exp_false)  
  
**Arguments:**  

**exp_cond**  
Expression to test.  
**exp_true**  
Expression specifying value to return if exp_cond is nonzero.  
**exp_false**  
Expression specifying value to return if exp_cond is zero.
  
  
**Return type:**  
Type of exp_true or exp_false, whichever is returned.  
  
**Error conditions:**  
Returns bottom if exp_cond evaluates to bottom, or if exp_true or exp_false  
(whichever is actually used) evaluates to bottom.  
  
Example:  
```  
value = Cond(var(3),1,2)  
; Sets value to 1 if var(3) is not zero, and sets value to 2 if var(3) is 0.  
```

---

## ConsecutiveWins (new)

Returns number of matches won consecutively by this team side. The counter increases for the winning team at the same time MatchOver trigger starts returning 1. Losing a round resets the counter to 0 and prevents increment for this match.

>Format:  
>ConsecutiveWins  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = ConsecutiveWins > 0
```

---

## Const (old)

Returns the value of one of the player's constants.  
  
**Format:**  
Const(param_name)  
  
**Arguments:**  

**param_name**  
The name of the constant to check. Valid values are listed under Details.  
  
**Return type:**  
Depends on specified hit parameter. See Details.  
  
**Error conditions:**  
none  
  
**Details:**  
The following values of param_name return values specified in the `[Data]` group in the player's constants.  
  
- data.life: Returns value of the "life" parameter. (int)  
- data.power: Returns value of the "power" parameter. (int)  
- data.attack: Returns value of the "attack" parameter. (int)  
- data.defence: Returns value of the "defence" parameter. (int)  
- data.fall.defence_mul: Returns value of the defence multiplier, calculated as 100/(f+100), where f is the "fall.defence_up" parameter. (float)  
- data.liedown.time: Returns value of the "liedown.time" parameter. (int)  
- data.airjuggle: Returns value of the "airjuggle" parameter. (int)  
- data.sparkno: Returns value of the "sparkno" parameter. (int)  
- data.guard.sparkno: Returns value of the "guard.sparkno" parameter. (int)  
- data.KO.echo: Returns value of the "ko.echo" parameter. (int)  
- data.IntPersistIndex: Returns value of the "IntPersistIndex" parameter. (int)  
- data.FloatPersistIndex: Returns value of the "FloatPersistIndex" parameter. (int)  
  
The following values of param_name return values specified in the `[Size]` group in the player's constants.  
  
- size.xscale: Returns value of the "xscale" parameter. (float)  
- size.yscale: Returns value of the "yscale" parameter. (float)  
- size.ground.back: Returns value of the "ground.back" parameter. (int)  
- size.ground.front: Returns value of the "ground.front" parameter. (int)  
- size.air.back: Returns value of the "air.back" parameter. (int)  
- size.air.front: Returns value of the "air.front" parameter. (int)  
- size.height: Returns value of the "height" parameter. (int)  
- size.attack.dist: Returns value of the "attack.dist" parameter. (int)  
- size.proj.attack.dist: Returns value of the "proj.attack.dist" parameter. (int)  
- size.proj.doscale: Returns value of the "proj.doscale" parameter. (int)  
- size.head.pos.x: Returns x-component of the "head.pos" parameter. (int)  
- size.head.pos.y: Returns y-component of the "head.pos" parameter. (int)  
- size.mid.pos.x: Returns x-component of the "mid.pos" parameter. (int)  
- size.mid.pos.y: Returns y-component of the "mid.pos" parameter. (int)  
- size.shadowoffset: Returns value of the "shadowoffset" parameter. (int)  
- size.draw.offset.x: Returns x-component of the "draw.offset" parameter. (int)  
- size.draw.offset.y: Returns y-component of the "draw.offset" parameter. (int)  
  
The following values of param_name return values specified in the `[Velocity]` group in the player's constants.  
  
- velocity.walk.fwd.x: Returns value of the "walk.fwd" parameter. (float)  
- velocity.walk.back.x: Returns value of the "walk.back" parameter. (float)  
- velocity.run.fwd.x: Returns x-component of the "run.fwd" parameter. (float)  
- velocity.run.fwd.y: Returns y-component of the "run.fwd" parameter. (float)  
- velocity.run.back.x: Returns x-component of the "run.back" parameter. (float)  
- velocity.run.back.y: Returns y-component of the "run.back" parameter. (float)  
- velocity.jump.y: Returns y-component of the "jump.neu" parameter. Note: this is NOT "velocity.jump.neu.y". Only the "neu" parameters take a y-component value. (float)  
- velocity.jump.neu.x: Returns x-component of the "jump.neu" parameter. (float)  
- velocity.jump.back.x: Returns value of the "jump.back" parameter. (float)  
- velocity.jump.fwd.x: Returns value of the "jump.fwd" parameter. (float)  
- velocity.runjump.back.x: Returns value of the "runjump.back" parameter. (float)  
- velocity.runjump.fwd.x: Returns value of the "runjump.fwd" parameter. (float)  
- velocity.airjump.y: Returns y-component of the "airjump.neu" parameter. Note: this is NOT "velocity.airjump.neu.y". (float)  
- velocity.airjump.neu.x: Returns x-component of the "airjump.neu" parameter. (float)  
- velocity.airjump.back.x: Returns value of the "airjump.back" parameter. (float)  
- velocity.airjump.fwd.x: Returns value of the "airjump.fwd" parameter. (float)  
- velocity.air.gethit.groundrecover.x: Returns x-component of the "air.gethit.groundrecover" parameter. (float)  
- velocity.air.gethit.groundrecover.y: Returns y-component of the "air.gethit.groundrecover" parameter. (float)  
- velocity.air.gethit.airrecover.mul.x: Returns x-component of the "air.gethit.airrecover.mul" parameter. (float)  
- velocity.air.gethit.airrecover.mul.y: Returns x-component of the "air.gethit.airrecover.mul" parameter. (float)  
- velocity.air.gethit.airrecover.add.x: Returns x-component of the "air.gethit.airrecover.add" parameter. (float)  
- velocity.air.gethit.airrecover.add.y: Returns x-component of the "air.gethit.airrecover.add" parameter. (float)  
- velocity.air.gethit.airrecover.back: Returns value of the "air.gethit.airrecover.back" parameter. (float)  
- velocity.air.gethit.airrecover.fwd: Returns value of the "air.gethit.airrecover.fwd" parameter. (float)  
- velocity.air.gethit.airrecover.up: Returns value of the "air.gethit.airrecover.up" parameter. (float)  
- velocity.air.gethit.airrecover.down: Returns value of the "air.gethit.airrecover.down" parameter. (float)  
  
The following values of param_name return values specified in the `[Movement]` group in the player's constants.  
  
- movement.airjump.num: Returns value of the "airjump.num" parameter. (int)  
- movement.airjump.height: Returns value of the "airjump.height" parameter. (int)  
- movement.yaccel: Returns value of the "yaccel" parameter. (float)  
- movement.stand.friction: Returns value of the "stand.friction" parameter. (float)  
- movement.crouch.friction: Returns value of the "crouch.friction" parameter. (float)  
- movement.stand.friction.threshold: Returns value of the "stand.friction.threshold" parameter. (float)  
- movement.crouch.friction.threshold: Returns value of the "crouch.friction.threshold" parameter. (float)  
- movement.jump.changeanim.threshold: Returns value of the "jump.changeanim.threshold" parameter. (float)  
- movement.air.gethit.groundlevel: Returns value of the "air.gethit.groundlevel" parameter. (float)  
- movement.air.gethit.groundrecover.ground.threshold: Returns value of the "air.gethit.groundrecover.ground.threshold" parameter. (float)  
- movement.air.gethit.groundrecover.groundlevel: Returns value of the "air.gethit.groundrecover.groundlevel" parameter. (float)  
- movement.air.gethit.airrecover.threshold: Returns value of the "air.gethit.airrecover.threshold" parameter. (float)  
- movement.air.gethit.airrecover.yaccel: Returns value of the "air.gethit.airrecover.yaccel" parameter. (float)  
- movement.air.gethit.trip.groundlevel: Returns value of the "air.gethit.trip.groundlevel" parameter. (float)  
- movement.down.bounce.offset.x: Returns x-component of the "down.bounce.offset.x" parameter. (float)  
- movement.down.bounce.offset.y: Returns y-component of the "down.bounce.offset.y" parameter. (float)  
- movement.down.bounce.yaccel: Returns value of the "down.bounce.yaccel" parameter. (float)  
- movement.down.bounce.groundlevel: Returns value of the "down.bounce.groundlevel" parameter. (float)  
- movement.down.friction.threshold: Returns value of the "down.friction.threshold" parameter. (float)  
  
Example:  
```  
trigger1 = Const(velocity.walk.fwd.x) > 4  
; Triggers if the forward walking velocity is greater than 4.  
```

---

## Const (changed)

The Const trigger can now also read Ikemen GO's [new constants](../Character-features/#cns_constants).

### Const(constants)

Returns the value of one of the player's constants from the [[Constants]](Character-features/#cns_constants) section.

```ini
[Constants]
FireballState = 1000

[State -1, Fireball]
triggerall = NumHelper(Const(FireballState)) = 0
```


### data.dizzypoints

Returns the value of the player's [Data] [dizzypoints](Character-features/#cns_data_dizzypoints) constant.

### data.fall.defence_up

Returns the value of the player's [Data] fall.defence_up constant.

### data.guardpoints

Returns the value of the player's [Data] [guardpoints](Character-features/#cns_data_guardpoints) constant.

### data.guardsound.channel

Returns the value of the player's [Data] [guardsound.channel](Character-features/#cns_data_guardsoundchannel) constant.

### data.hitsound.channel

Returns the value of the player's [Data] [hitsound.channel](Character-features/#cns_data_hitsoundchannel) constant.

### size.height.crouch

Returns the value of the player's [Size] [height.crouch](Character-features/#cns_size_height_crouch) constant.

### size.height.air.top

Returns the first value of the player's [Size] [height.air](Character-features/#cns_size_height_air) constant.

### size.height.air.bottom

Returns the second value of the player's [Size] [height.air](Character-features/#cns_size_height_air) constant.

### size.height.down

Returns the value of the player's [Size] [height.down](Character-features/#cns_size_height_down) constant.

### velocity.air.gethit.ko.add

Returns the value of the player's [Velocity] [air.gethit.ko.add](Character-features/#cns_velocity_airgethitkoadd) constant.
* `velocity.air.gethit.ko.add.x`
* `velocity.air.gethit.ko.add.y`
* `velocity.air.gethit.ko.add.z`

### velocity.air.gethit.ko.ymin

Returns the value of the player's [Velocity] [air.gethit.ko.ymin](Character-features/#cns_velocity_airgethitkoymin) constant.

### velocity.ground.gethit.ko.xmul

Returns the value of the player's [Velocity] [ground.gethit.ko.xmul](Character-features/#cns_velocity_groundgethitkoxmul) constant.

### velocity.ground.gethit.ko.add

Returns the value of the player's [Velocity] [ground.gethit.ko.add](Character-features/#cns_velocity_groundgethitkoadd) constant.
* `velocity.ground.gethit.ko.add.x`
* `velocity.ground.gethit.ko.add.y`
* `velocity.ground.gethit.ko.add.z`

### velocity.ground.gethit.ko.ymin

Returns the value of the player's [Velocity] [ground.gethit.ko.ymin](Character-features/#cns_velocity_groundgethitkoymin) constant.

---

## Const1080p (new)

Converts a value from the 1080p coordinate space to the player's coordinate space. The conversion ratio between coordinate spaces is the ratio of their widths.

>Format:  
>Const1080p(exprn)  
>  
>Arguments:  
>exprn  
>Expression containing the value to convert. (float)  
>  
>Return type:  
>float  

```ini
value = Const1080p(12)
  Sets value 2 if the player has a coordinate space of 320x240 (240p).
  Sets value 4 if the player has a coordinate space of 640x480 (480p).
  Sets value 8 if the player has a coordinate space of 1280x720 (720p).
  Sets value 12 if the player has a coordinate space of 1920x1080 (1080p).
```

---

## Const240p (old)

Converts a value from the 240p coordinate space to the player's coordinate space.  
The conversion ratio between coordinate spaces is the ratio of their widths.  
  
**Format:**  
Const240p(exprn)  
  
**Arguments:**  
*exprn*  
Expression containing the value to convert. (float)
  
**Return type:**  
float  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom.  
  
**Notes:**  
Non-zero position and velocity offset values in common1.cns should use one of  
the `Const` triggers to maintain consistency with characters from a different  
coordinate space.  
  
Example:  
```  
value = Const240p(3)  
; Sets value 3 if the player has a coordinate space of 320x240 (240p).  
; Sets value 6 if the player has a coordinate space of 640x480 (480p).  
; Sets value 12 if the player has a coordinate space of 1280x720 (720p).  
```

---

## Const480p (old)

Converts a value from the 480p coordinate space to the player's coordinate space.  
The conversion ratio between coordinate spaces is the ratio of their widths.  
  
**Format:**  
Const480p(exprn)  
  
**Arguments:**  

**exprn**  
Expression containing the value to convert. (float)
  
  
**Return type:**  
float  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom.  
  
**Notes:**  
Non-zero position and velocity offset values in common1.cns should use one of the `Const` triggers to maintain consistency with characters from a different  
coordinate space.  
  
Example:  
```  
value = Const480p(6)  
; Sets value 3 if the player has a coordinate space of 320x240 (240p).  
; Sets value 6 if the player has a coordinate space of 640x480 (480p).  
; Sets value 12 if the player has a coordinate space of 1280x720 (720p).  
```

---

## Const720p (old)

Converts a value from the 720p coordinate space to the player's coordinate space.  
The conversion ratio between coordinate spaces is the ratio of their widths.  
  
**Format:**  
Const720p(exprn)  
  
**Arguments:**  

**exprn**  
Expression containing the value to convert. (float)
  
  
**Return type:**  
float  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom.  
  
**Notes:**  
Non-zero position and velocity offset values in common1.cns should use one of the `Const` triggers to maintain consistency with characters from a different coordinate space.  
  
Example:  
```  
value = Const720p(12)  
; Sets value 3 if the player has a coordinate space of 320x240 (240p).  
; Sets value 6 if the player has a coordinate space of 640x480 (480p).  
; Sets value 12 if the player has a coordinate space of 1280x720 (720p).  
```

---

## Cos (math) (old)

Computes the cosine of the specified argument (in radians.)  
  
**Format:**  
cos(exprn)  
  
**Arguments:**  

**exprn**  
Expression to compute the cosine of. (float)
  
  
**Return type:**  
float  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom.  
  
Example:  
```  
value = cos(0)  
; Sets value to the cosine of 0, which is approximately 1.0 (possibly with some rounding error.)  
```

---

## Ctrl (old)

Returns the control flag of p1.  
  
**Format:**  
Ctrl  
  
**Arguments:**  
none  
  
**Return type:**  
boolean int (1 or 0)  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = Ctrl  
; Triggers if the player has control.  
```

---

## DebugMode (new)

Returns information related to the debug mode.

>Format:  
>DebugMode(param_name)  
>  
>Arguments:  
>param_name  
>The name of the parameter to check. Valid values are:  
>accel, clsndisplay, debugdisplay, lifebarhide, wireframedisplay, roundrestarted

```ini
trigger1 = DebugMode(accel) != 0
trigger1 = DebugMode(clsndisplay)
```

---

## DecisiveRound (new)

Returns 1 if the match will conclude if the player's team wins.

>Format:  
>DecisiveRound  
>  
>Arguments:  
>none  
>  
>Return type:  
>boolean int (1 or 0)  

```ini
trigger1 = DecisiveRound
```

---

## Defence (new)

Returns the player's current defence value. This value accounts for all defence multipliers.

>Format:  
>Defence  
>  
>Arguments:  
>none  
>  
>Return type:  
>float  

```ini
trigger1 = Defence = 100
```

---

## DefenceMul (new)

Returns the player's current defencemul value.

>Format:  
>DefenceMul
>  
>Arguments:  
>none  
>  
>Return type:  
>float  

```ini
trigger1 = DefenceMul > 1.0
```

---

## Deg (Math) (new)

Converts an argument value from radians to degrees.

>Format:  
>Deg(exp)  
>  
>Arguments:  
>exp  
>Expression  
>  
>Return type:  
>float  

```ini
trigger1 = Deg(pi/2) = 90
```

---

## DisplayName (new)

Returns the player's displayed name. Note that the lifebar name is not necessarily the same.

>Format:  
>DisplayName [oper] "name"  
>  
>Arguments:  
>[oper]  
>=, != (other operators not valid)  
>  
>"name" (string)  
>Name to compare against. Must be in double quotes.  
>  
>Return type:  
>boolean int (1 or 0)  

```ini
trigger1 = EnemyNear, DisplayName = "Gopher"
```

---

## Dizzy (new)

Returns 1 if character is under [dizzy effect](Miscellaneous-Info/#dizzy) (assigned by [DizzySet](State-controllers-(new)/#new_dizzyset) sctrl).

>Format:  
>Dizzy  
>  
>Arguments:  
>none  
>  
>Return type:  
>boolean int (1 or 0)  

```ini
trigger1 = !Dizzy
```

---

## DizzyPoints (new)

Returns the amount of [dizzy points](Character-features/#dizzypoints) the player has.

>Format:  
>DizzyPoints  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = DizzyPoints = 0
```

---

## DizzyPointsMax (new)

Returns the maximum amount of [dizzy points](Character-features/#dizzypoints) the player can have. This is normally the same value as LifeMax (adjustable in character's CNS `[Data]` section).

>Format:  
>DizzyPointsMax  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = DizzyPoints < DizzyPointsMax / 2
```

---

## DrawGame (old)

Returns 1 if the player (or the player's team, in team mode) has ended the round in a draw, 0 otherwise.  
  
**Format:**  
Draw  
  
**Arguments:**  
none  
  
**Return type:**  
boolean int (1 or 0)  
  
**Error conditions:**  
none  
  
Examples:  
```  
trigger1 = DrawGame  
; Triggers if the player (or team) ended round in a draw.  
```

---

## DrawPal (new)

returns the value of the group and index of the palette being used to draw the sprites at the moment, unlike PalNo, which returns the palette selected in the character select screen. 

>Format:  
>DrawPal 
> 
>Arguments:  
>group, index  
>  
>Return type:  
>int  

```ini
[State -2, PowerAdd]
type = PowerAdd
trigger1 = DrawPal group = 1 && DrawPal Index = 12
value = 30
```

---

## E (math) (old)

Returns the value of e (2.718281828...)  
  
**Format:**  
e  
  
**Arguments:**  
none  
  
**Return type:**  
float  
  
**Error conditions:**  
none

---

## EnvShakeVar (new)

Allows checking the (remaining) time, frequency and amplitude of the current EnvShake.

>Format:  
>EnvShakeVar  
>  
>Arguments:  
>param_name  
>The name of the constant to check. Valid values are: time, freq, ampl  
>  
>Return type:  
>float  

```ini
trigger1 = EnvShakeVar(time) = 1
trigger2 = EnvShakeVar(freq) = 60
trigger3 = EnvShakeVar(ampl) = -4
```

---

## Exp (math) (old)

Computes the exponential of the argument (e raised to the power of the argument.) This produces slightly more accurate results than the equivalent expression e**(argument).  
  
**Format:**  
exp(exprn)  
  
**Arguments:**  

**exprn**  
Expression to compute the exponential of (float).
  
  
**Return type:**  
float  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom.  
  
Example:  
```  
value = exp(4-var(0))  
; Sets value to e raised to the quantity 4-var(0).  
```

---

## ExplodVar (new)

Returns the specified explod parameter. Use -1 for ID to iterate over all explods.

>Format:  
>ExplodVar(id, index, param)  
>  
>Arguments:  
>id  
>Expression 1  
>  
>index  
>Expression 2  
>  
>param  
>Valid values are accel x, accel y, anim, animelem, animelemtime, angle, angle x, angle y, bindid, bindtime, facing, drawpal group, drawpal index, ID, layerno, pausemovetime, pos x, pos y, removetime, scale x, scale y, sprpriority, time, vel x, vel y  
>  
>Return type:  
>int or float

---

## Facing (old)

Returns 1 if the player is facing to the right, and -1 if the player is facing to the left.  
  
**Format:**  
Facing  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
Example:  
```  
Trigger = Facing = -1  
; Triggers if the player is facing toward the left of the screen.  
```

---

## FightScreenState (new)

Allows checking if the fight screen is displaying specific screens.  

>Format:  
>FightScreenState(param)
>  
>Arguments:  
>param  
>The parameter to check. See details   

Details:
* `fightdisplay`: Returns true if the fight call is being displayed. (bool)
* `kodisplay`: Returns true if the KO screen is being displayed. (bool)
* `rounddisplay`: Returns true if the round number screen is being displayed. (bool)
* `windisplay`: Returns true if the winner announcement screen is being displayed. (bool)

Example:  
```ini
trigger1 = FightScreenState(rounddisplay) = 1
trigger2 = FightScreenState(fightdisplay) = 1
```

---

## FightScreenVar (new)

Returns information about the fight screen (commonly referred to as "lifebars").

>Format:  
>FightScreenVar(param_name)  
>  
>Arguments:  
>param_name  
>The name of the parameter to check. Valid values are:  
>info.author, info.localcoord.x, info.localcoord.y, info.name, round.ctrl.time, round.over.hittime, round.over.time, round.over.waittime, round.over.wintime, round.slow.time, round.start.waittime, round.callfight.time, time.framespercount  

Refer to lifebar documentation and examples for the function of each argument.

```ini
trigger1 = FightScreenVar(Info.Name) = "Some lifebar"
trigger1 = FightScreenVar(Info.LocalCoord.X) = 1280
trigger1 = Time > FightScreenVar(Round.Ctrl.Time)
```

---

## FightTime (new)

Returns the amount of ticks since the start of the actual fight.

>Format:  
>FightTime  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = FightTime > 600
```

---

## FirstAttack (new)

Returns 1 if this character has landed the first attack (before any of the opponents or team partners) in the current round. Otherwise returns 0.

>Format:  
>FirstAttack  
>  
>Arguments:  
>none  
>  
>Return type:  
>boolean int (1 or 0)  

```ini
trigger1 = FirstAttack
```

---

## Float (math) (new)

Converts argument evaluating to int type into float type.

>Format:  
>Float(exp)  
>  
>Arguments:  
>exp  
>Expression  
>  
>Return type:  
>float  

```ini
fvar(10) = Float(Life) / LifeMax
```

---

## Floor (math) (old)

Implements the floor function. Returns the greatest integer less than or equal to its argument.  
  
**Format:**  
floor(exprn)  
  
**Arguments:**  

**exprn**  
Expression to compute the floor of.
  
  
**Return type:**  
int  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom.  
  
Examples:  
```  
value=floor(5.5)  
; Sets value to 5.  

value=floor(-2)  
; Sets value to -2.  
```

---

## FrontEdge (old)

FrontEdge returns the x position of the edge of the screen that is in front the player, in absolute stage coordinates.  
  
**Format:**  
FrontEdge  
  
**Arguments:**  
none  
  
**Return type:**  
float  
  
**Error conditions:**  
none  
  
**Notes:**  
This trigger is equivalent to the expression "ifelse(facing = 1, RightEdge, LeftEdge)".  
  
Example:  
```  
trigger1 = facing * (Pos X + CameraPos X) < facing * (FrontEdge)  
; Triggers if the player is behind the front edge of the screen.  
```

---

## FrontEdgeBodyDist (old)

FrontEdgeBodyDist gives the distance between the front of the player (as determined by the front edge of his width bar) and the edge of the screen.  
  
**Format:**  
FrontEdgeBodyDist  
  
**Arguments:**  
none  
  
**Return type:**  
float  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = FrontEdgeBodyDist < 30  
; Triggers if the front of the player is within 30 pixels  
  of the edge of the screen in front of him.  
```

---

## FrontEdgeDist (old)

FrontEdgeDist gives the distance between the x-axis of the player and the edge of the screen in front of the player.  
  
**Format:**  
FrontEdgeDist  
  
**Arguments:**  
none  
  
**Return type:**  
float  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = FrontEdgeDist < 30  
; Triggers if the x-axis of the player is within 30 pixels  
  of the edge of the screen in front of him.  
```

---

## FVar (old)

This trigger takes a mandatory variable number as an argument. It returns the value of the player's specified float variable.  
  
**Format:**  
FVar(exprn)  
  
**Arguments:**  

**exprn**  
An expression evaluating to a variable number. Valid numbers  
at this time are 0-39.
  
  
**Return type:**  
float  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom, or if exprn evaluates  
to an invalid variable index.  
  
Example:  
```  
trigger1 = FVar(5) = -1.23  
; Triggers if the value of float variable 5 is -1.23.  
```

---

## GameHeight (old)

Returns the current height of the game space in the player's local coordinate space.  
The game space is defined as the currently-visible area of the stage in which players interact.  
The dimensions of the game space at a zoom factor of 1.0 is specified by the  
GameWidth and GameHeight parameters in mugen.cfg.  
  
**Format:**  
GameHeight  
  
**Arguments:**  
none  
  
**Return type:**  
float  
  
**Error conditions:**  
none  
  
**Notes:**  
GameWidth and GameHeight scale inversely with the zoom factor of the camera.  
For example, if the camera zoom factor is 0.5, the values returned by GameWidth and GameHeight will be double that of at zoom factor 1.  
ScreenWidth and ScreenHeight are the equivalent triggers that are not affected by the camera zoom factor.  
  
  
Example:  
```  
trigger1 = ScreenPos Y < GameHeight / 2  
; Triggers if the player is above the center of the screen.  
```

---

## GameHeight (changed)

If mugenVersion is specified as 1.0 in character's [[Info]](Character-features/#def_info) section, GameHeight returns the same value as ScreenHeight.

---

## GameMode (new)

Returns the current game mode.

>Format:  
>GameMode [oper] "name"  
>  
>Arguments:  
>[oper]  
>=, != (other operators not valid)  
>  
>"name" (string)  
>Name to compare against. Must be in double quotes.  
>  
>Return type:  
>boolean int (1 or 0)  

```ini
trigger1 = GameMode = "arcade"
```

The following game modes are detectable by default:
- arcade
- bonus
- bossrush
- challenger
- demo
- freebattle
- netplaysurvivalcoop
- netplayteamcoop
- netplayversus
- randomtest
- survival
- survivalcoop
- teamcoop
- timeattack
- training
- versus
- versuscoop
- watch

The trigger can be also used to detect [story mode arcs](Miscellaneous-Info/#arcs) and modes added via [external modules](Miscellaneous-Info/#lua_modules).

---

## GameOption (new)

Allows checking the various game options as defined in config.ini (TBD)
Keep in mind that until string support is added to the engine, only numeric values are useful to return.

>Format:  
>GameOption  
>  
>Arguments:  
>param_name  
>The name of the variable to check.
>  
>Return type:  
>variable

```ini
trigger1 = GameOption(sound.wavchannels) = 32
```

---

## GameTime (old)

Returns the total number of ticks that have elapsed in the game so far.  
  
**Format:**  
GameTime  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = (GameTime % 27) = 0  
  Triggers every 27th game tick.  
```

---

## GameVar (new)

Allows checking some system variables that generally don't justify having their own dedicated triggers.  

>Format:  
>GameVar(param)
>  
>Arguments:  
>param  
>The parameter to check. See details   

Details:
* `introtime`: Returns the internal timer that controls pre-fight screens. (int)
* `outrotime`: Returns the internal timer that controls post-fight screens. (int)
* `pausetime`: Returns the time that the game is under the effect of `Pause`. (int)
* `slowtime`: Returns the time that the game is under the effect of KO slowdown. (int)
* `superpausetime`: Returns the time that the game is under the effect of `SuperPause`. (int)
* `persistrounds`: Returns `1` if the round persist flag is active. (int)
* `persistlife`: Returns `1` if the life persist flag is active. (int)
* `persistmusic`: Returns `1` if the music persist flag is active. (int)
* `hidebars`: Returns `1` if the hidebars flag is active. (int)

Example:  
```ini
trigger1 = GameVar(superpausetime) = 0
trigger2 = GameVar(introtime) = FightScreenVar(round.ctrl.time)
```

---

## GameWidth (old)

Returns the current width of the game space in the player's local coordinate space.  
The game space is defined as the currently-visible area of the stage in which players interact.  
The dimensions of the game space at a zoom factor of 1.0 is specified by the GameWidth and GameHeight parameters in `mugen.cfg`.  
  
**Format:**  
GameHeight  
  
**Arguments:**  
none  
  
**Return type:**  
float  
  
**Error conditions:**  
none  
  
**Notes:**  
GameWidth and GameHeight scale inversely with the zoom factor of the camera.  
For example, if the camera zoom factor is 0.5, the values returned by GameWidth and GameHeight will be double that of at zoom factor 1.  
ScreenWidth and ScreenHeight are the equivalent triggers that are not affected by the camera zoom factor.  
  
Example:  
```  
trigger1 = ScreenPos X >= GameWidth / 2  
; Triggers if the player is to the right of the center of the screen.  
```

---

## GameWidth (changed)

If mugenVersion is specified as 1.0 in character's [[Info]](Character-features/#def_info) section, GameWidth returns the same value as ScreenWidth.

---

## GetHitVar (old)

When the player is in a gethit state, returns the value of the specified hit parameter.  
  
**Format:**  
GetHitVar(param_name)  
  
**Arguments:**  

**param_name**  

**The name of the hit parameter to check. Valid values are:**  
xveladd, yveladd, type, animtype, airtype, groundtype, damage,  
hitcount, fallcount, hitshaketime, hittime, slidetime, ctrltime,  
recovertime, xoff, yoff, zoff, xvel, yvel, yaccel, hitid,  
chainid, guarded, fall, fall.damage, fall.xvel, fall.yvel,  
fall.recover, fall.time, fall.recovertime.
  
  
**Return type:**  
Depends on specified hit parameter. See Details.  
  
**Error conditions:**  
none  
  
**Details:**  
- xveladd: Returns the additional x-velocity that is added to the player's own when he is KOed. (float)  
- yveladd: Returns the additional y-velocity that is added to the player's own when he is KOed. (float)  
- type: Returns the type of the hit: 0 for none, 1 for high, 2 for low, 3 for trip (ground only).  
- animtype: Returns the animation type of the hit. (0 for light, 1 for medium, 2 for hard, 3 for back, 4 for up, 5 for diag-up)  
- airtype: Returns the type specified in the HitDef for an air hit.  
- groundtype: Returns the type specified in the HitDef for a ground hit.  
- damage: Returns the damage given by the hit. (int)  
- hitcount: Returns the number of hits taken by the player in current combo. (int)  
- fallcount: Returns the number of times player has hit the ground in the current combo. (int)  
- hitshaketime: Returns time player is "frozen" during the hit. This number counts down by 1 for each game tick, and stops when it reaches zero. (int)  
- hittime: Returns time before player regains control and returns to an idle state after being hit.  
This counts down by 1 per game tick, as long as hitshaketime (see above) is greater than 0. It stops counting down when the value reaches -1. (int) `GetHitVar(hittime) < 0` is equivalent to the `HitOver` trigger.  
- slidetime: Returns time that player slides backwards (on the ground) after the hit. (int)  
- ctrltime: Returns time before player regains control after guarding the hit. (int)  
- recovertime: Returns time before player gets up from liedown state. This number counts down to 0 for each game tick, and will count down faster if buttons are hit. (int)  
- xoff: "Snap" x offset when hit (deprecated)  
- yoff: "Snap" y offset when hit (deprecated)  
- xvel: Fixed x-velocity imparted by hit. (float)  
- yvel: Fixed y-velocity imparted by hit. (float)  
- yaccel: y acceleration set by the hit. (float)  
- chainid: Player-assigned chainID for last hit taken. (int)  
- guarded: True if the last hit was guarded, false otherwise.  
- isbound: True if the player is the subject of an attacker's TargetBind controller. Useful to prevent being stuck in thrown states. (int)  
- fall: True if falling, false otherwise (int)  
- fall.damage: Damage taken upon fall (int)  
- fall.xvel: x velocity after bouncing off ground (float)  
- fall.yvel: y velocity after bouncing off ground (float)  
- fall.recover: True if player can recover, false otherwise.  
- fall.recovertime: time before player can recover. (int)  
- fall.kill: value of fall.kill parameter in attacker's hitdef. (int)  
- fall.envshake.time: See below. (int)  
- fall.envshake.freq: See below. (float)  
- fall.envshake.ampl: See below. (int)  
- fall.envshake.phase: Returns values set by the fall.envshake.\* parameters in an attacker's hitdef. (float)  
  
Example:  
```  
trigger1 = GetHitVar(yvel) < -5.5  
; Triggers if the hit's specified y velocity is less than -5.5.  
```

---

## GetHitVar (changed)

### air.velocity.x (y, z) (nightly build only)

Returns the X, Y or Z component of the last HitDef's `air.velocity` parameter, even if the player was not hit in the air. (float)


### airguard.velocity.x (y, z) (nightly build only)

Returns the X, Y or Z component of the last HitDef's `airguard.velocity` parameter, even if the player did not guard in the air. (float)


### air.animtype, fall.animtype, ground.animtype

Returns the literal value specified in the HitDef.


### attr (nightly build only)

Returns the last HitDef `attr` assignment. Requires a comparison to known flags. (string)  

```ini
trigger1 = getHitVar(attr) = SCA, HA
```


### dizzypoints

Returns last HitDef `dizzypoints` value. (int)


### down.velocity.x (y, z) (nightly build only)

Returns the X, Y or Z component of the last HitDef's `down.velocity` parameter, even if the player was not hit while down. (float)


### facing (nightly build only)

Returns last HitDef `p2facing` value. (int)


### fall.envshake.mul

Returns last HitDef `fall.envshake.mul` value. (float)


### fall.zvel (nightly build only)

Returns z velocity after bouncing off ground (float)


### frame (nightly build only)

Returns true only during the same frame where the player got hit by an attack. (bool)


### ground.velocity.x (y, z) (nightly build only)

Returns the X, Y or Z component of the last HitDef's `ground.velocity` parameter, even if the player was not hit on the ground. (float)


### guard.velocity.x (y, z) (nightly build only)

Returns the X, Y or Z component of the last HitDef's `guard.velocity` parameter, even if the player did not guard on the ground. (float)  


### guardpoints

Returns last HitDef `guardpoints` value. (int)


### guardcount (nightly build only)

Returns how many hits the player has guarded without a chance to fight back. (int)


### guarddamage

Returns the second value of the last HitDef's `damage` parameter. (int)


### guardflag (nightly build only)

Returns the `guardflag` parameter of the last HitDef that hit the player. Requires a comparison to known flags. (string)  

```ini
trigger1 = getHitVar(guardflag) = L
```


### guardko (nightly build only)

Returns 1 if the player was KO'd by guard damage. (bool)


### guardpower

Returns the second value of the last HitDef's `givepower` parameter. In other words, the power received when guarding. (int)


### hitflag (nightly build only)

Returns the `hitflag` parameter of the last HitDef that hit the player. Requires a comparison to known flags. (string)  

```ini
trigger1 = getHitVar(hitflag) = MA
```


### hitpower

Returns the first value of the last HitDef's `givepower` parameter. In other words, the power received when getting hit. (int)


### hitdamage

Returns the first value of the last HitDef's `damage` parameter. (int)


### kill

Returns the kill flag of the last hit or LifeAdd the character suffered. (int)


### playerid

Returns the ID of the last character that hit the player. (int)  
Note: Up until Ikemen GO version 0.99, this trigger used `ID` syntax instead of `playerID`. That syntax is still valid, but it's deprecated.  


### playerno

Returns the [PlayerNo](Triggers-(new)/#new_playerno) of the last character that hit the player. (int)


### power (nightly build only)

Returns how much power the player received from the last hit, regardless of getting hit or guarding. (int)


### priority (nightly build only)

Returns the numerical value of the attack priority of the last HitDef. (int)


### projid (nightly build only)

Returns the `projID` of the last projectile that hit the player. Returns -1 if not hit by a projectile. (int)


### redlife

Returns last HitDef `redlife` value. (int)


### score

Returns last HitDef `score` value. (float)


### teamside (nightly build only)

Returns the `teamside` of the last HitDef that hit the player. (int)


### type

Returns the value of either groundtype or airtype, depending on the character's StateType upon being hit. Such a trigger was documented in Mugen but did not work.


### xaccel (nightly build only)

Returns the X acceleration set by the hit. (float)  
NOTE: Currently, this parameter will only work if the character does not override the `common1.cns.zss` states that use it.  


### xveladd (nightly build only)

This trigger was dummied out in Mugen, always returning 0. In Ikemen, it works as documented.


### yveladd (nightly build only)

This trigger was dummied out in Mugen, always returning 0. In Ikemen, it works as documented.


### zaccel (nightly build only)

Returns the Z acceleration set by the hit. (float)  
NOTE: Currently, this parameter will only work if the character does not override the `common1.cns.zss` states that use it.  


### zvel (nightly build only)

Returns the fixed z-velocity imparted by hit. (float)


### zoff (nightly build only)

"Snap" z offset when hit.

---

## GroundAngle (new)

TODO: ? Related to undocumented [PlatformAngle](State-controllers-(changed)/#changed_projectile_platformangle) projectile parameter.

>Format:  
>GroundAngle  
>  
>Arguments:  
>none  
>  
>Return type:  
>float  

```ini
trigger1 = GroundAngle != 0
```

---

## GroundLevel (new)

Returns the character's ground level, which is normally 0 but can be changed via [GroundLevelOffset](State-controllers-(new)/#new_groundleveloffset).  
  
>Format:  
>GroundLevel
>  
>Arguments:  
>none  
>  
>Return type:  
>float

---

## GuardBreak (new)

Returns 1 if character is under [guard break](Miscellaneous-Info/#guardbreak) (assigned by [GuardBreakSet](State-controllers-(new)/#new_guardbreakset) sctrl).

>Format:  
>GuardBreak  
>  
>Arguments:  
>none  
>  
>Return type:  
>boolean int (1 or 0)  

```ini
trigger1 = !GuardBreak
```

---

## GuardCount (new)

Returns how many hits of the current attack were guarded. Similar to Hitcount.

>Format:  
>GuardCount  
>  
>Arguments:  
>none  
>  
>Return type:  
>int

```ini
trigger1 = GuardCount >= 2
```

---

## GuardPoints (new)

Returns the amount of [guard points](Character-features/#guardpoints) the player has.

>Format:  
>GuardPoints  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = GuardPoints = 0
```

---

## GuardPointsMax (new)

Returns the maximum amount of [guard points](Character-features/#guardpoints) the player can have. This is normally the same value as LifeMax (adjustable in character's CNS `[Data]` section).

>Format:  
>GuardPointsMax  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = GuardPoints < GuardPointsMax / 2
```

---

## HelperIndexExist(n) (new)

Returns 1 if a player's helper with the specified index number exists, or 0 otherwise.

```ini
trigger1 = HelperIndexExist(5)
trigger1 = HelperIndex(5),time > 0
```

---

## HelperName (new)

Returns the helper's name (assigned via helper's name parameter, which defaults to "\<parent\>'s helper" if a unique name is not assigned).

>Format:  
>HelperName [oper] "name"  
>  
>Arguments:  
>[oper]  
>=, != (other operators not valid)  
>  
>"name" (string)  
>Name to compare against. Must be in double quotes.  
>  
>Return type:  
>boolean int (1 or 0)  

```ini
trigger1 = HelperName = "Fireball"
```

---

## HelperVar (new)

Returns a helper's unique properties. If called from a root player, the return is always invalid.  

>Format:  
>helpervar(param)
>  
>Arguments:  
>param  
>The parameter to check. See details  
>  
>Return type:  
>Varies. See details  

Details:
* `clsnproxy`: Returns clsnproxy `ID` parameter (bool)
* `helpertype`: Returns the `helpertype` parameter as an int. Returns 1 for `normal`, 2 for `player` and 3 for `projectile` (int)
* `ID`: Returns the `ID` parameter (int)
* `keyctrl`: Returns the `keyctrl` parameter (bool)
* `ownclsnscale`: Returns the `ownclsnscale` parameter (bool)
* `ownpal`: Returns the `ownpal` parameter (bool)
* `preserve`: Returns the `preserve` parameter (bool)

Example:  
```ini
trigger1 = Helper(1000), HelperVar(keyctrl)
```

---

## HitByAttr (new)

Checks if the player can be hit by an attack with the specified attribute.  
See also documentation for the `attr` parameter in `HitDef` as well as `HitDefAttr`.  

>Format:  
>HitByAttr(flag1, flag2)  
>  
>Arguments:  
>flag1  
>The state type flag.  
>  
>flag2  
>The attack type flag.  
>  
>Return type:  
>boolean int (1 or 0)  

Note: Because `HitBy` and `NotHitBy` often last only one frame, player processing order can have a great influence in the return of this trigger.  

Example:
```ini
trigger1 = HitByAttr(S, NT); Returns true if the player can be hit by standing throws
```

---

## HitCount (old)

Returns the number times the player's current attack move has hit one or more opponents. This value is valid only for a single state; after any state change, it resets to 0. To prevent it from resetting to 0, set hitcountpersist in the StateDef (see cns documentation for details). The HitCount and UniqHitCount triggers differ only when the player is hitting more than one opponent. In the case where the player is hitting two opponents with the same attack, HitCount will increase by 1 for every hit, while UniqHitCount increases by 2.  
  
**Format:**  
HitCount  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = HitCount > 8  
; Triggers when more than 8 hits have been dealt to the  
  opponent since the start of the player's attack move.  
```

---

## HitDefAttr (old)

Checks the attribute parameter of the player's currently-active HitDef.  
If the player is not currently attacking, then no parameters will match.  
Can be used for simple move-interrupts from weaker to stronger attacks in the CMD file.  
Note: `HitDefAttr != value1, value2` is logically equivalent to `!(HitDefAttr = value1, value2)`.  
  
**Format:**  
HitDefAttr [oper] value1, value2  
  
**Arguments:**  

**[oper]**  
=, !=  
**value1**  
A string that has at least one of the letters "S", "C"  
and "A" for standing, crouching and aerial attacks  
respectively. For example, "SA" is for standing and  
aerial attacks.  
**value2**  
A set of 2-character strings, separated by commas.  
Each 2-character string must be of the form described:  
The first character is either "N" for "normal", "S" for  
"special", or "H" for "hyper". The second character must  
be either "A" for "attack" (a normal hit attack) or "T"  
for "throw". For example, "NA, ST" is for normal attacks  
and special throws.  
Assuming the attribute of the player's HitDef is in the form `arg1, arg2`, then the trigger condition is determined to be true only if arg1 is a subset of value1, AND arg2 is a subset of value2.  
See the "attr" parameter of the HitDef controller in Appendix B for details.  
  
**Return type:**  
boolean int (1 or 0)  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = HitDefAttr = A, HA  
; Triggers when the player is in an attack state, where the current HitDef has the following attributes:  
; 1. is an aerial attack and 2. is a hyper (super) attack  
  
trigger1 = HitDefAttr = SC, NA, SA  
; Triggers when the player is in an attack state, where the current HitDef has the following attributes:  
; 1. is either a standing or a crouching attack and 2. is either a normal attack or a special attack  
```

---

## HitDefVar (new)

Returns information about the player's currently active HitDef or ReversalDef. The parameter format is the same as in the `HitDef` state controller.  
Note: When the player has no active HitDef or ReversalDef, this trigger will return the default values of each parameter. It is generally advised to check if a HitDef or ReversalDef is active first with `HitDefAttr` or `ReversalDefAttr`.  

>Format:  
>HitDefVar(param)
>  
>Arguments:  
>param  
>
>The parameter to check. Valid values:  
>See details  
>  
>Return type:  
>Varies. See details  

Details:
* `guard.dist.depth.bottom`: Returns the guard distance in the z-axis, under the char
* `guard.dist.depth.top`: Returns the guard distance in the z-axis, above the char
* `guard.dist.height.bottom`: Returns the guard distance in the y-axis, under the char
* `guard.dist.height.top`: Returns the guard distance in the y-axis, above the char
* `guard.dist.width.back`: Returns the guard distance in the x-axis, behind the char
* `guard.dist.width.front`: Returns the guard distance in the x-axis, in front of the char
* `guard.pausetime`: Returns the first value of the Hitdef's `guard.pausetime` parameter (int)
* `guard.sparkno`: The guard spark animation number (int)
* `guard.shaketime`: Returns the second value of the Hitdef's `guard.pausetime` parameter (int)
* `guarddamage`: Returns the second value of the Hitdef's `damage` parameter (int)
* `guardflag`: Checks if the specified flags exist in the Hitdef's `guardflag`. Valid flags `HLMAFDP+-` (bool)
* `guardsound.group`: Returns the guard sound's group (first value) (int)
* `guardsound.number`: Returns the guard sound's number (second value) (int)
* `hitdamage`: Returns the first value of the Hitdef's `damage` parameter (int)
* `hitflag`: Checks if the specified flags exist in the Hitdef's `hitflag`. Valid flags `HLMAFDP+-` (bool)
* `hitsound.group`: Returns the hit sound's group (first value) (int)
* `hitsound.number`: Returns the hit sound's number (second value) (int)
* `id`: Returns the Hitdef's `id` parameter (int)
* `p1stateno`: Returns the Hitdef's `p1stateno` parameter (int)
* `p2stateno`: Returns the Hitdef's `p2stateno` parameter (int)
* `pausetime`: Returns the first value of the Hitdef's `pausetime` parameter (int)
* `priority`: Returns the first value of the Hitdef's `priority` parameter (int)
* `shaketime`: Returns the second value of the Hitdef's `pausetime` parameter (int)
* `sparkno`: Returns the hit spark animation number (int)
* `sparkx`: Returns the X component of the Hitdef's `sparkxy` parameter (float)
* `sparky`: Returns the Y component of the Hitdef's `sparkxy` parameter (float)
* `xaccel`: Returns the Hitdef's `xaccel` parameter (float)
* `yaccel`: Returns the Hitdef's `yaccel` parameter (float)
* `zaccel`: Returns the Hitdef's `zaccel` parameter (float)
* `ground.velocity.x`: Returns the X component of the Hitdef's `ground.velocity` parameter (float)
* `ground.velocity.y`: Returns the Y component of the Hitdef's `ground.velocity` parameter (float)
* `ground.velocity.z`: Returns the Z component of the Hitdef's `ground.velocity` parameter (float)
* `air.velocity.x`: Returns the X component of the Hitdef's `air.velocity` parameter (float)
* `air.velocity.y`: Returns the Y component of the Hitdef's `air.velocity` parameter (float)
* `air.velocity.z`: Returns the Z component of the Hitdef's `air.velocity` parameter (float)
* `down.velocity.x`: Returns the X component of the Hitdef's `down.velocity` parameter (float)
* `down.velocity.y`: Returns the Y component of the Hitdef's `down.velocity` parameter (float)
* `down.velocity.z`: Returns the Z component of the Hitdef's `down.velocity` parameter (float)
* `guard.velocity.x`: Returns the X component of the Hitdef's `guard.velocity` parameter (float)
* `guard.velocity.y`: Returns the Y component of the Hitdef's `guard.velocity` parameter (float)
* `guard.velocity.z`: Returns the Z component of the Hitdef's `guard.velocity` parameter (float)
* `airguard.velocity.x`: Returns the X component of the Hitdef's `airguard.velocity` parameter (float)
* `airguard.velocity.y`: Returns the Y component of the Hitdef's `airguard.velocity` parameter (float)
* `airguard.velocity.z`: Returns the Z component of the Hitdef's `airguard.velocity` parameter (float)
* `ground.cornerpush.veloff`: Returns the Hitdef's `ground.cornerpush.veloff` parameter (float)
* `air.cornerpush.veloff`: Returns the Hitdef's `air.cornerpush.veloff` parameter (float)
* `down.cornerpush.veloff`: Returns the Hitdef's `down.cornerpush.veloff` parameter (float)
* `guard.cornerpush.veloff`: Returns the Hitdef's `guard.cornerpush.veloff` parameter (float)
* `airguard.cornerpush.veloff`: Returns the Hitdef's `airguard.cornerpush.veloff` parameter (float)
* `fall.velocity.x`: Returns the X component of the Hitdef's `fall.velocity` parameter (float)
* `fall.velocity.y`: Returns the Y component of the Hitdef's `fall.velocity` parameter (float)
* `fall.velocity.z`: Returns the Z component of the Hitdef's `fall.velocity` parameter (float)

Notes:
* `guardflag` and `hitflag` are not simply a direct reading of the Hitdef's parameter. That is to say `HitDefVar(guardflag) = L` returns true whether the Hitdef's guardflag is `L`, `M` or `MA` for example.  

Example:  
```ini
trigger1 = HitDefVar(hitdamage) >= 100
trigger2 = P2, HitDefVar(guardflag) = L; attack can be blocked crouching
trigger3 = P2, HitDefVar(guardflag) != H; attack cannot be blocked standing
```

---

## HitFall (old)

If the player is currently in a gethit state, returns the fall flag of the hit. The output of this trigger is undefined if the player is not in a gethit state. For an explanation of the fall flag, see the HitDef documentation.  
  
**Format:**  
HitFall  
  
**Arguments:**  
none  
  
**Return type:**  
boolean int (1 or 0)  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = !HitFall  
; Triggers if the hit did not put the player into a fall state.  
```

---

## HitOver (old)

If the player is in a gethit state, returns 1 when the hittime has expired, and 0 otherwise. For an explanation of hittime, see the HitDef documentation.  
  
**Format:**  
HitOver  
  
**Arguments:**  
none  
  
**Return type:**  
boolean int (1 or 0)  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = HitOver = 1  
; Triggers when the player’s hittime has expired.  
```

---

## HitOverridden (new)

Returns 1 during frame in which player has overridden default gethit behavior via HitOverride state controller. Otherwise returns 0.

>Format:  
>HitOverridden  
>  
>Arguments:  
>none  
>  
>Return type:  
>boolean int (1 or 0)  

```ini
trigger1 = HitOverridden
```

---

## HitPauseTime (old)

Returns the time until the player's hitpause expires.  
The player enters a hitpause when his attack comes in contact with an opponent.  
The initial hitpause time is equal to the first value of the pausetime parameter in the player's HitDef.  
If `ignorehitpause` is not set, this will always return 0.  
  
**Format:**  
HitPauseTime  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = HitPauseTime = 0  
; Triggers when the player is not paused for a hit.  
```

---

## HitShakeOver (old)

If the player is in a gethit state, returns 1 if the hit shake (the period when he is shaking in place) has ended, and 0 otherwise.  
  
**Format:**  
HitShakeOver  
  
**Arguments:**  
none  
  
**Return type:**  
boolean int (1 or 0)  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = HitShakeOver = 0  
; Triggers if the player is still shaking from the hit.  
```

---

## HitVel (old)

Gets the value of the velocity imparted to the player by a hit.  
You must specify the component that you want to check, eg. `HitVel Y` to check the vertical velocity component.  
  
**Format:**  
HitVel [component]  
  
**Arguments:**  

**[component]**  
X, Y
  
  
**Return type:**  
float  
  
**Error conditions:**  
none  
  
**Details:**  
A positive HitVel Y means that the player is moving upward on the screen.  
A positive HitVel X means that the player is moving backward.  
Note that the HitVel X trigger behaves in the opposite manner to the Vel X trigger.  
  
Example:  
```  
trigger1 = HitVel X > 0.5  
; True when the player's gethit x-velocity is greater than 0.5  
  pixels per tick.  
```

---

## ID (old)

Returns the ID number of the player.  
The ID number is unique for every player throughout the course of a match.  
Any helper that is created during this time will also receive its own unique ID number.  
This trigger may be useful for getting opponents' ID numbers, to be later used with the "playerID" redirection keyword (see exp docs). Do not confuse playerID with targetID.  
  
**Format:**  
ID  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
Example:  
```  
value = ID  
  This sets value to the ID number of the current player.  
value = EnemyNear, ID  
  This sets value to the ID number of the nearest opponent.  
```

---

## IfElse (math) (old)

This trigger takes three arguments. If the first is nonzero, `IfElse` returns the value of the second argument. Else, it returns the value of the third argument.  
All arguments are evaluated prior to execution of IfElse. In particular, any side effects caused by evaluation of the arguments (such as variable assignment, or performing a computation that generates a warning) will occur.  
If you wish to avoid these side effects, then use `Cond`.  
  
**Format:**  
IfElse(exp_cond,exp_true,exp_false)  
  
**Arguments:**  

*exp_cond*  
Expression to test.  
*exp_true*  
Expression specifying value to return if exp_cond is nonzero.  
*exp_false*  
Expression specifying value to return if exp_cond is zero.
  
  
**Return type:**  
Type of exp_true or exp_false, whichever is returned.  
  
**Error conditions:**  
Returns bottom if exp_cond evaluates to bottom, or if exp_true or exp_false (whichever is returned) evaluates to bottom.  
  
Example:  
```  
value = ifelse(var(3),1,2)  
; Sets value to 1 if var(3) is not zero, and sets value to 2 if var(3) is 0.  
```

---

## IkemenVersion (new)

Returns the character's Ikemen version as a float.  
For example, a character with `ikemenversion = 0.98.2` in its DEF file will have `IkemenVersion` return `0.982000`.  

>Format:  
>IkemenVersion  
>  
>Arguments:  
>none  
>  
>Return type:  
>float  

```ini
trigger1 = P2, IkemenVersion < 0.99
```

---

## InCustomAnim (new)

Returns 1 if the character is in a custom animation, such as when `ChangeAnim2` is used in a custom state.  

>Format:  
>InCustomAnim  
>  
>Arguments:  
>none  
>  
>Return type:  
>boolean int (1 or 0)  

```ini
trigger1 = InCustomAnim
```

---

## InCustomState (new)

Returns 1 if the character is in a custom state (sent into another player's state).

>Format:  
>InCustomState  
>  
>Arguments:  
>none  
>  
>Return type:  
>boolean int (1 or 0)  

```ini
trigger1 = InCustomState
```

---

## Index (new)

Returns the player's index as an integer. See [PlayerIndex](Triggers-(new)/#redirection_playerindex).

---

## InDialogue (new)

Returns 1 during ongoing dialogue initiated by [Dialogue](State-controllers-(new)/#new_dialogue) state controller.

>Format:  
>InDialogue  
>  
>Arguments:  
>none  
>  
>Return type:  
>boolean int (1 or 0)  

```ini
trigger1 = InDialogue
```

---

## InGuardDist (old)

Returns 1 if the player is within guarding distance of an opponent's physical or projectile attack. The guarding distance is the value of the guard.dist parameter of the opponent's HitDef. Returns 0 if out of guard distance, or the opponent is not attacking.  
  
**Format:**  
InGuardDist  
  
**Arguments:**  
none  
  
**Return type:**  
boolean int (1 or 0)  
  
**Error conditions:**  
none  
**Example:**  
none

---

## InputTime (new)

Returns number of frames since a given button was pressed or released. A positive number means the button is being held, while a negative number means it has been released. For players without `keyctrl`, it returns 0.  

This time advances regardless of the player being paused.  

>Format:  
>InputTime(button)  
>  
>Arguments:  
>button  
>The button to check. Valid values are:  
>B, F, D, U, a, b, c, x, y, z, s, d, w, m, L, R  
>These are the four cardinal directional inputs (B, F, D, U); the six attack buttons (a, b, c, x, y, z); start (s); the two new attack/tag buttons (d, w); the select/back/menu button (m); and absolute left/right directional inputs (L, R).  

```ini
trigger1 = InputTime(F) > 0; forward is being held
trigger2 = InputTime(U) < 0; up is not being held
trigger3 = InputTime(a) = 1; a was just pressed
trigger4 = InputTime(b) = 30; b has been held for 30 frames
trigger5 = InputTime(c) = -40; c was released 40 frames ago
```

---

## IntroState (new)

Returns the current intro state number:  
0: Not applicable, or players have gained ctrl after "fight!"  
1: Pre-intro (RoundState = 0)  
2: Player intros (RoundState = 1)  
3: Round announcement  
4: Fight called  

>Format:  
>IntroState  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = IntroState = 3
```

---

## IsAsserted (new)

Returns 1 if the character has specified AssertSpecial state controller flag asserted. Flags that affect all characters at once don't have to be asserted directly by character to be detectable.

>Format:  
>IsAsserted(flag_name)  
>  
>Arguments:  
>flag_name  
>The name of the AssertSpecial state controller flag to check (string).  
>  
>Return type:  
>boolean int (1 or 0)  

```ini
trigger1 = IsAsserted(noBG)
```

---

## IsClsnProxy (new)

Returns if the helper is a [Clsn Proxy](./State-controllers-(changed)#clsnproxy).

>Format:  
>IsClsnProxy
>
>Arguments:
>none
>
>Return type:
>boolean int (1 or 0)

```ini
trigger1 = IsClsnProxy
```

---

## IsHelper (old)

This trigger takes an optional ID number as an argument.  
If the ID number is omitted, IsHelper returns 1 if the player is a helper character, and 0 otherwise.  
If the ID number is included, then IsHelper returns 1 if the player is a helper character with the specified ID number, and 0 otherwise.  
  
**Format:**  
- IsHelper  
- IsHelper(exprn)  
  
**Arguments:**  
none  
  
**Return type:**  
boolean int (1 or 0)  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom.  
  
Examples:  
```  
1. trigger1 = !IsHelper  
; Triggers if the player is not a helper-type character.  
2. trigger1 = IsHelper(1234)  
; Triggers if the player is a helper character with ID number 1234.  
```

---

## IsHelper (changed)

The `IsHelper` trigger now also accepts an optional index argument, through the new format `IsHelper(ID, index)`. Defaults to -1 (any index).  
The old formats still work exactly the same.  

Example:
```ini
trigger1 = IsHelper(123, 2); Is the third helper with ID 123
```

---

## IsHomeTeam (old)

Returns 1 if the player's team is considered the "home team".  
In arcade modes, the computer is always considered the home team.  
In versus modes, P1's side (left) is the home team.  
  
**Format:**  
IsHomeTeam  
  
**Arguments:**  
none  
  
**Return type:**  
boolean int (1 or 0)  
  
**Error conditions:**  
none  
**Example:**  
none

---

## IsHost (new)

Returns if the player is host in online match.

>Format:  
>IsHost  
>  
>Arguments:  
>none  
>  
>Return type:  
>boolean int (1 or 0)  

```ini
trigger1 = IsHost
```

---

## JugglePoints (new)

Returns the remaining juggle points between the player and another player with the specified ID. If the specified ID is not yet a target of the first player, the trigger will simply return the maximum juggle points.

>Format:  
>JugglePoints(exprn)
>  
>Arguments:  
>exprn
>An expression evaluating to a player ID number (int).
>  
>Return type:  
>int

```ini
trigger1 = JugglePoints(EnemyNear, ID) < 10
```

---

## LastPlayerID (new)

Returns the ID number of the last spawned player or helper.

>Format:  
>LastPlayerID
>  
>Arguments:  
>none  
>  
>Return type:  
>int

```ini
trigger1 = PlayerID(LastPlayerID), HitDefAttr = SCA, AP
```

---

## LayerNo (new)

Returns the layer number on which the character is currently being drawn on.

>Format:  
>LayerNo
>  
>Arguments:  
>none  
>  
>Return type:  
>int

```ini
trigger1 = LayerNo = -1
```

---

## LeftEdge (old)

LeftEdge returns the x position of the left edge of the screen, in absolute stage coordinates.  
  
**Format:**  
LeftEdge  
  
**Arguments:**  
none  
  
**Return type:**  
float  
  
**Error conditions:**  
none  
  
**Notes:**  
This trigger is equivalent to the expression `CameraPos X - GameWidth / 2`.  
  
Example:  
```  
trigger1 = Pos X + CameraPos X < LeftEdge  
; Triggers if the player is to the left of the left edge of the screen.  
```

---

## Lerp (Math) (new)

Linear interpolation. Takes three arguments, and returns a number between two specified arguments at a specific increment. 

>Format:  
>Lerp(a,b,amount)  
>  
>Arguments:  
>a  
>Expression 1  
>  
>b  
>Expression 2  
>  
>amount(Avaiable range 0-1)  
>Expression 3  
>  
>Return type:  
>float  

```ini
trigger1 = Lerp(0, 100, 0.5) = 50
```

---

## Life (old)

Returns the player's life.  
  
**Format:**  
Life  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = life <= 10  
; Triggers if the player has 10 or less life points remaining.  
```

---

## LifeMax (old)

Returns the maximum amount of life the player can have. This is normally the value of the `life` parameter in the [Data] group of the player variables, but may be different in situations such as team modes.  
  
**Format:**  
LifeMax  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = life < lifemax / 4  
; Triggers if the player has less than 1/4 of his maximum life.  
```

---

## Ln (math) (old)

Returns the natural logarithm of its argument. This produces slightly more accurate results than the otherwise equivalent expression log(e,(argument)).  
  
**Format:**  
ln(exprn)  
  
**Arguments:**  

**exprn**  
Expression to compute the natural logarithm of (float).
  
  
**Return type:**  
float  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom, or if exprn is not  
positive.  
  
Example:  
```  
value = ln(time)  
  Sets value to the natural logarithm of the player's statetime.  
```

---

## LocalCoord (new)

Returns the character's `localcoord` as a float. This trigger returns a constant value even when the player is in a custom state.

>Format:  
>LocalCoord [component]  
>  
>Arguments:  
>[component]  
>X, Y  
>  
>Return type:  
>float  

```ini
trigger1 = LocalCoord X < Enemy, LocalCoord Y
```

---

## Log (math) (old)

Takes two arguments a and b, and returns the base-a logarithm of b.  
  
**Format:**  
Log(exp1,exp2)  
  
**Arguments:**  

**exp1**  
Expression giving the base of the logarithm. Must be positive.  
**exp2**  
Expression giving the value to take the logarithm of. Must be  
positive.
  
  
**Return type:**  
float  
  
**Error conditions:**  
Returns bottom if either of exp1 or exp2 evaluates to bottom, or if  
either of exp1 or exp2 is not positive.  
  
Example:  
```  
value=log(2,64)  
  Sets value to the base 2 log of 64, which is 6.0.  
```

---

## Lose (old)

Returns 1 if the player (or the player's team, in team mode) has lost the round, 0 otherwise. Can be suffixed with "KO" or "Time" to return 1 only when the round has been lost by a KO or by time expiring, respectively.  
  
**Format:**  
- Lose  
- LoseKO  
- LoseTime  
  
**Arguments:**  
none  
  
**Return type:**  
boolean int (1 or 0)  
  
**Error conditions:**  
none  
  
Examples:  
```  
1. trigger1 = Lose  
; Triggers if the player (or his team) has lost the round.  
  
2. trigger1 = !LoseKO  
; Triggers if the player (or his team) has not lost the round by  
  a KO. For example, this will trigger if the player's team has  
  not yet lost the round, or if they have lost the round by time  
  over.  
```

---

## Map (new)

Use the name of the map you want to recognize in parentheses. For example, a character with the below map will return Map(age) as a value set in character DEF file or via various state controllers that can modify character's map. If nothing is set, 0 is returned.

>Format:  
>Map  
>  
>Arguments:  
>name  
>Name of the map  
>  
>Return type:  
>float  

```ini
trigger1 = Map(age) >= 18
```

---

## MatchNo (old)

Returns the current match number.  
  
**Format:**  
MatchNo  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Details:**  
The current match number is always 1 in versus-type modes. In Arcade and Team Arcade modes, the match number starts at 1 and increments every time a new match starts (does not increment on continue). If you finish the arcade mode and start a new game, the match number reverts to 1.  
**Example:**  
none

---

## MatchOver (old)

Returns 1 if the match has ended. (For example, in the case of a best-of-three match, this will return true when one of the players or teams has won two rounds.)  
  
**Format:**  
MatchOver  
  
**Arguments:**  
none  
  
**Return type:**  
boolean int (1 or 0)  
  
**Error conditions:**  
none  
  
**Details:**  
Currently, MatchOver does not return true until the players start their win poses (state 180). This behavior may be subject to change in future releases.  
  
Example:  
```  
trigger1 = !matchover  
; Triggers if the match is not over. For instance, the current round  
  may not yet have ended, or it may have ended without deciding the  
  match.  
```

---

## Max (math) (new)

Takes two arguments, and returns the highest-valued number.

>Format:  
>Max(exp1,exp2)  
>  
>Arguments:  
>exp1  
>Expression 1  
>  
>exp2  
>Expression 2  
>  
>Return type:  
>float  

```ini
trigger1 = Max(var(3), 10)
```

---

## MemberNo (new)

Returns character's team member position. Team leader is 1, while partners receive successive numbers. In Tag mode this value is dynamic.  

>Format:  
>MemberNo  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = MemberNo = 1
```

---

## Min (math) (new)

Takes two arguments, and returns the lowest-valued number.

>Format:  
>Min(exp1,exp2)  
>  
>Arguments:  
>exp1  
>Expression 1  
>  
>exp2  
>Expression 2  
>  
>Return type:  
>float  

```ini
trigger1 = Min(var(3), 10)
```

---

## MotifState (new)

Allows retrieval of whether the specified post-round sequence is active.  

>Format:  
>MotifState(parameter)
>  
>Arguments:  
>parameter  
>The name of the motif state to check. Valid values are:  
>challenger, continuescreen, continueyes, continueno, demo, dialogue, menu, victoryscreen, winscreen, hiscore   
>  
>Return type:  
>boolean int (1 or 0)

---

## MotifVar (new)

Allows checking the various screenpack options as defined in system.def (TBD)
Keep in mind that until string support is added to the engine, only numeric values are useful to return.

>Format:  
>MotifVar  
>  
>Arguments:  
>param_name  
>The name of the variable to check.
>  
>Return type:  
>variable

```ini
trigger1 = MotifVar(info.mugenversion) >= 1
```

---

## MoveContact (old)

This trigger is valid only when the player is in an attack state.  
MoveContact gives a non-zero value if P2 has either been hit, or has guarded P1's attack. It gives 0 otherwise. P1 is the player, and P2 is his opponent.  
Typically used with the `StateNo` and `Command` triggers for detecting move-interrupts in the CMD file.  
  
**Format:**  
MoveContact  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
**Details:**  
On attack contact, MoveContact returns 1.  
After contact, MoveContact's return value will increase by 1 for each game tick that P1 is not paused (P1 gets paused on contact; see pausetime parameter in HitDef controller).  
The values of MoveGuarded, MoveHit and MoveReversed increment in the same fashion.  
Note 1: the values of MoveContact, MoveGuarded, MoveHit and MoveReversed are set simultaneously. For example, if one HitDef in a move hits successfully, MoveHit will return non-zero. If a following HitDef in the same move is guarded, MoveGuarded will return non-zero, and the other three triggers will return 0.  
Note 2: the values of the four Move\* triggers reset to 0 and stop incrementing after a state transition. See `movehitpersist` parameter for StateDefs (CNS docs) for how to override this behavior.  
  
  
Examples:  
```  
trigger1 = MoveContact  
  True if P1's attack did not miss P2.  
  
trigger1 = MoveContact = 1  
  True from the time P1's attack came in contact with P2, until just after P1's pausetime wears off.  
```

---

## MoveCountered (new)

This trigger is valid only when the player is in an attack state. MoveCountered returns 1 on attack contact, at the exact frame that p1 interrupts p2 attack (true for 1 frame, even if both P1 and P2 countered each other's moves). After contact, MoveCountered's return value will increase by 1 for each game tick that P1 is not paused. It gives 0 otherwise. See Details section of Mugen's `MoveContact` trigger for more information.

>Format:  
>MoveCountered  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = MoveCountered = 1
```

---

## MoveGuarded (old)

This trigger is valid only when the player is in an attack state.  
MoveGuarded gives a non-zero value if P2 is guarding, or has guarded, P1's attack. It gives 0 otherwise. P1 is the player, and P2 is his opponent.  
Typically used with the `StateNo` and `Command` triggers for detecting move-interrupts in the CMD file.  
  
**Format:**  
MoveGuarded  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
**Details:**  
See Details section for MoveContact trigger.  
  
Example:  
```  
trigger1 = MoveGuarded  
; True if P1's attack was guarded by P2.  
```

---

## MoveHit (old)

This trigger is valid only when the player is in an attack state.  
MoveHit gives a non-zero value if P2 has been hit by P1's attack. It gives 0 otherwise.  
Typically used with the `StateNo` and `Command` triggers for detecting move-interrupts in the CMD file.  
  
**Format:**  
MoveHit  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
**Details:**  
See Details section for MoveContact trigger.  
  
Example:  
```  
trigger1 = MoveHit  
  True if P1's attack connected successfully with P2.  
```

---

## MoveHitVar (new)

Similarly to `GetHitVar`, this trigger allows retrieving information about the last hit the player inflicted.  
This trigger works even if that hit acquired no `target`.  

>Format:  
>MoveHitVar(parameter)
>  
>Arguments:  
>parameter  
>The name of the hit parameter to check. Valid values are:  
>cornerpush.veloff, frame, overridden, playerid, playerno, sparkx, sparky, uniqhit  
>  
>Return type:  
>Varies. See details

Details:
* `cornerpush.veloff`: Returns the stored velocity offset used for cornerpush. (float)  
* `frame`: Returns true only during the same frame where the player connected an attack. (bool)  
* `overridden`: Returns true if the last hit encountered a HitOverride. (bool)  
* `playerid`: Returns ID of the last player hit by the HitDef. (int)  
* `playerno`: Returns the player number of the last player hit by the HitDef. (int)  
* `sparkx`: Returns the horizontal offset of the hitsparks created by the Hitdef. (float)  
* `sparky`: Returns the vertical offset of the hitsparks created by the Hitdef. (float)  
* `uniqhit`: Returns the number of players the last HitDef connected against. (int)  

Notes:
* Unlike `MoveHit`, `MoveHitVar(frame)` updates during a hitpause.
* `MoveHitVar(sparkx)` and `MoveHitVar(sparky)` offsets are relative to the attacking player's position.

Example:
```ini
[State FX]
type = explod
trigger1 = MoveHit = 1
trigger1 = MoveHitVar(Frame) = 1
postype = p1
pos = MoveHitVar(SparkX), MoveHitVar(SparkY)
```

---

## MoveReversed (old)

This trigger is valid only when the player is in an attack state.  
MoveReversed gives a non-zero value if P1's attack has been reversed by P2. It gives 0 otherwise.  
  
**Format:**  
MoveReversed  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
**Details:**  
See Details section for MoveContact trigger.  
  
Example:  
```  
trigger1 = MoveReversed  
  True if P1's attack was reversed by P2.  
```

---

## MoveType (old)

MoveType gives the player's move-type. Refer to the section on StateDef in the CNS documentation for more details on MoveType.  
Useful for "move interrupts" in the CMD file.  
  
**Format:**  
MoveType [oper] move_type  
  
**Arguments:**  

**[oper]**  
=, !=   (other operators not valid)  
**move_type (char)**  

**A, I, H**  
Attack, Idle and GetHit move-types respectively.
  
  
**Return type:**  
boolean int (1 or 0)  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = movetype != H  
; Triggers if the player is not currently in a gethit-type state.  
```

---

## MugenVersion (new)

Returns the character's Mugen version as a float.  
Returns 1.1 for characters with an Ikemen version, regardless of what's specified in the def file.  
Currently returns 0.5 for WinMugen characters, but checking if version is < 1.0 is better advised.  

MugenVersion >= 1.0 is equivalent to MajorVersion.

>Format:  
>MugenVersion  
>  
>Arguments:  
>none  
>  
>Return type:  
>float  

```ini
trigger1 = MugenVersion = 1.1
```

---

## Name (old)

Returns the player's name (the internal name specified in the .DEF file, which may not be the same as the displayed name).  
  
**Format:**  
Name [oper] "name"  
  
**Arguments:**  

**[oper]**  
=, != (other operators not valid)  
**"name" (string)**  
Name to compare against. Must be in double quotes.
  
  
**Return type:**  
boolean int (1 or 0)  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = Name = "Kumquat"  
  Returns true if the player is named Kumquat.  
```

---

## NumEnemy (old)

NumEnemy returns the number of opponents that exist. Neutral players and normal helpers are not considered opponents.  
  
**Format:**  
NumEnemy  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
Examples:  
```  
trigger1 = NumEnemy = 2  
trigger1 = enemynear(1), name = "Squash"  
; Triggers if there are 2 opponents, and the second-closest one is named Squash.  
```

---

## NumExplod (old)

This trigger takes an ID number as an optional argument.  
If the ID number is omitted, NumExplod returns the number of explods owned by the player.  
If the ID number is included, then NumExplod returns the number of explods with that ID number that are owned by the player.  
The ID number must be greater than -1. An ID number of -1 or less will give the same behavior as if the ID number is omitted.  
  
**Format:**  
- NumExplod  
- NumExplod(exprn)  
  
**Arguments:**  

**exprn**  
Expression evaluating to an ID number (int).
  
  
**Return type:**  
int  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom.  
  
Examples:  
```  
1. trigger1 = NumExplod >= 4  
; Triggers if the player currently owns 4 or more explods.  
2. trigger1 = NumExplod(1234) >= 4  
; Triggers if the player currently owns 4 or more explods with ID  
  1234.  
```

---

## NumHelper (old)

This trigger takes an ID number as an optional argument.  
If the ID number is omitted, then NumHelper returns the total number of helpers currently owned by the player.  
If the ID number is included, then NumHelper returns the total number of helpers with that ID number owned by the player.  
The ID number must be greater than 0. If the ID number is 0 or less, then all helpers are counted.  
  
**Format:**  
- NumHelper  
- NumHelper(exprn)  
  
**Arguments:**  

**exprn**  
Expression evaluating to an ID number (int).
  
  
**Return type:**  
int  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom.  
  
Examples:  
```  
1. trigger1 = NumHelper < 2  
; Triggers if the player now has less than 2 helpers.  
2. trigger1 = NumHelper(1234) < 2  
; Triggers if the player now has less than 2 helpers with ID 1234.  
```

---

## NumPartner (old)

NumPartner returns the number of partners that exist. Neutral players and normal helpers are not considered partners.  
  
**Format:**  
NumPartner  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
Examples:  
```  
trigger1 = NumPartner = 1  
trigger1 = partner, life < 200  
; Triggers if the player has a partner with less than 200 life  
```

---

## NumPlayer (new)

Returns total number of players (including helpers, attached chars, etc) existing ingame.

```ini
trigger1 = NumPlayer > 5
```

---

## NumProj (old)

Returns the total number of projectiles currently owned by the player.  
  
**Format:**  
NumProj  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = NumProj = 0  
; Triggers if the player has no currently active projectiles.  
```

---

## NumProjID (old)

This trigger takes an ID number as a required argument. It returns the number of projectiles currently owned by the player and having the specified ID number.  
  
**Format:**  
NumProjID(exprn)  
  
**Arguments:**  

**exprn**  
Expression evaluating to an ID number.
  
  
**Return type:**  
int  
  
**Error conditions:**  
If a negative ID is specified, then the ID defaults to 0. Returns  
bottom if exprn evaluates to bottom.  
  
Example:  
```  
trigger1 = NumProjID(1234) = 1  
; Triggers if there the player currently owns exactly 1 projectile  
  with the ID number 1234.  
```

---

## NumStageBG (new)

Returns the number of BG elements in the stage that have the specified ID. If the ID argument is not used, or if ID is -1, it returns the total.  

>Format:  
>1. NumStageBG  
>2. NumStageBG(ID)  
>
>Arguments:  
>ID  
>Expression evaluating to an ID number (int)  
>
>Return type:  
>int  

Example:
```go
if numStageBG > 0 {
	for i = 0; numStageBG(-1) - 1; 1 {
		modifyStageBG{
			ID: -1;
			index: $i;
			pos.x: randomRange(-10, 10);
			pos.y: randomRange(-10, 10);
		}
	}
}
```

---

## NumTarget (old)

This trigger takes an ID number as an optional argument. If the ID number is omitted, NumTarget returns the current number of targets for the player. If the ID number is included, then NumTarget returns the number of targets for the player which have that target ID number. The ID number must be greater than -1. An ID number of -1 or less will give the same behavior as if the ID number is omitted.  
  
**Format:**  
- NumTarget  
- NumTarget(exprn)  
  
**Arguments:**  

**exprn**  
Expression evaluating to an ID number (int).
  
  
**Return type:**  
int  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom.  
  
Examples:  
```  
1. trigger1 = NumExplod >= 4  
; Triggers if the player currently owns 4 or more explods.  
2. trigger1 = NumExplod(1234) >= 4  
; Triggers if the player currently owns 4 or more explods with ID  
  1234.  
```

---

## NumText (new)

This trigger takes an ID number as an optional argument. If the ID number is omitted, NumText returns the number of texts owned by the player. If the ID number is included, then NumText returns the number of texts with that ID number that are owned by the player. The ID number must be greater than -1. An ID number of -1 or less will give the same behavior as if the ID number is omitted.

>Format:  
>1.NumText  
>2.NumText(exprn)  
>
>Arguments:  
>exprn  
>Expression evaluating to an ID number (int)  
>
>Return type:  
>int  

```ini
trigger1 = NumText >= 2
trigger1 = NumText(1234) >= 2
```

---

## Offset (new)

Returns the value of the player's x,y offset applied with OffSet sctrl.

>Format:  
>OffSet argument
>  
>Arguments:  
>x, y
>  
>Return type:
>float

```ini
trigger1 = OffSet x > 100 && OffSet y > 50
```

---

## OutroState (new)

Returns the current outro state number:  
0: Not applicable  
1: Payers can still act, allowing a possible double KO  
2: Players still have control, but the match outcome can no longer be changed  
3: Players lose control, but the round has not yet entered win states  
4: Player win states  
5: Round over (starting from the last frame of the RoundState sequence and continuing through the entire post-round sequence, individually detactable with [MotifState](https://github.com/ikemen-engine/Ikemen-GO/wiki/Triggers-(new)#motifstate-nightly-build-only) trigger)  

>Format:  
>OutroState  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = OutroState = 3
```

---

## P1Name (old)

This is an alias for the Name trigger. See "Name".

---

## P2BodyDist (old)

Returns the distance of P2 from P1, where P1 is the player, and P2 is his opponent. P2BodyDist is useful in the CMD for cases where P1 has an attack that is different when performed close to P2.  
  
**Format:**  
P2BodyDist [component]  
  
**Arguments:**  

**[component]**  
X, Y
  
  
**Return type:**  
float  
  
**Error conditions:**  
none  
  
**Details:**  
For comparing the Y-distance, P2BodyDist gives the difference in the  
heights of the players' Y-axes. A negative value means that P2 is  
above P1.  
For comparing the X-distance, P2BodyDist gives the  
X-distance of P2's front from P1's front. So, if the  
players are standing right next to each other, then  
P2BodyDist is 0. Remember that you can set the width of  
the player in "front.width", etc. under [Size] in the  
player variables.  
See also P2Dist.  
  
Example:  
```  
trigger1 = P2BodyDist X < 30  
; Triggers if the front of P2 is within 30 pixels of the front of  
  P1.  
```

---

## P2BodyDist (changed)

### Y (nightly build only)

In Mugen, this trigger merely does the same as `P2Dist Y`. If a character has `ikemenversion`, it will instead return the distance between the size boxes of the two players.

### Z (nightly build only)

P2BodyDist now also accepts a Z argument. When there is overlap between the players' Z width, it returns 0, otherwise returns the distance between their theoretical width boxes.

---

## P2Dist (old)

Returns the distance of P2 from P1, where P1 is the player, and P2 is his opponent.  
  
**Format:**  
P2Dist [component]  
  
**Arguments:**  

**[component]**  
X, Y
  
**Return type:**  
float  
  
**Error conditions:**  
none  
  
**Details:**  
For comparing the Y-distance, P2Dist gives the difference in the  
heights of the players' Y-axes. A negative value means that P2 is  
above P1.  
For comparing the X-distance, P2Dist gives the X-distance  
of P2's axis from P1's axis. A positive value indicates P2  
is in front of P1.  
See also P2BodyDist.  
  
Example:  
```  
trigger1 = P2Dist Y <= -12  
  True if P2 is at least 12 pixels higher up than P1.  
```

---

## P2Dist Z (changed)

The `P2Dist` trigger now also accepts a `Z` argument. Returns the distance between the players in the Z axis.

---

## P2Life (old)

Same as Life, except that this returns the opponent's life.

---

## P2MoveType (old)

Same as MoveType, except that this returns the opponent's movetype.

---

## P2Name (old)

Same as P1Name, except that this returns the name of the primary opponent (the opponent in versus mode, or the first opponent in team mode).  
If there is no primary opponent, then p2name = "name" returns 0 no  
matter what name is specified. Similarly, p2name != "name" will return 1 no matter what name is specified.

---

## P2StateNo (old)

Same as StateNo, except that this returns the opponent's state number.  
  
**Error conditions:**  
Returns bottom if p2 does not exist. (For instance, if the round  
has been won.)

---

## P2StateType (old)

Same as StateType, except that this returns the opponent's state type.  
  
**Error conditions:**  
Returns bottom if p2 does not exist. (For instance, if the round  
has been won.)

---

## P3Name (old)

Same as P1Name, except that this returns the name of the player's teammate, if present.  
If there is no teammate, then p3name = "name" returns 0 no matter what name is specified. Similarly, p3name != "name" will return 1 no matter what name is specified.

---

## P4Name (old)

Same as P1Name, except that this returns the name of the secondary opponent, if present.  
If there is no secondary opponent, then p4name = "name" returns 0 no matter what name is specified. Similarly, p4name != "name" will return 1 no matter what name is specified.

---

## P5Name, P6Name, P7Name, P8Name (new)

Same as P1Name-P4Name, except that these return the name of other team members, if present. If there is no such opponent, then it returns 0 no matter what name is specified. Similarly, P5Name != "name" will return 1 no matter what name is specified.

>Format:  
>PXName [oper] "name"  
>  
>Arguments:  
>[oper]  
>=, != (other operators not valid)  
>  
>"name" (string)  
>Name to compare against. Must be in double quotes.  
>  
>Return type:  
>boolean int (1 or 0)  

```ini
trigger1 = P5Name = "Kumquat"
```

---

## PalFXVar (new)

[TODO] Returns information about the player, background or global ("all") PalFX. Accepted parameters:

time  
add.r, add.g, add.b  
mul.r, mul.g, mul.b  
color, hue, invertall, invertblend  
bg.time  
bg.add.r, bg.add.g, bg.add.b  
bg.mul.r, bg.mul.g, bg.mul.b  
bg.color, bg.hue, bg.invertall  
all.time  
all.add.r, all.add.g, all.add.b  
all.mul.r, all.mul.g, all.mul.b  
all.color, all.hue, all.invertall, all.invertblend  

```ini
trigger1 = PalFXVar(add.r) != 0
  ;triggers when red has been added to the player via PalFX
```

---

## PalNo (old)

Returns the palette number of the player (i.e., the color scheme chosen for the character during character select.)  
  
**Format:**  
PalNo  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
**Details:**  
The palette ordering is specified in the character's def file.
If omitted, the default ordering is:
`A  B  C  X  Y  Z A2 B2 C2 X2 Y2 Z2`
`1  2  3  4  5  6  7  8  9 10 11 12`
  
Example:  
```  
trigger1 = PalNo = 5  
  Returns true if the current palette number is 5.  
```

---

## ParentDist (old)

This trigger is only valid for helper-type characters.  
ParentDist returns the distance from the helper to its parent. It works similarly to P2Dist.  
  
**Format:**  
ParentDist [component]  
  
**Arguments:**  

**[component]**  
X, Y
  
  
**Return type:**  
float  
  
**Error conditions:**  
Returns bottom if the player does not have a parent (e.g., if the  
parent was destroyed or KO'd).  
  
**Details:**  
For comparing the Y-distance, ParentDist gives the difference in the heights of the players' Y-axes. A negative value means that the parent is above its child.  
For comparing the X-distance, ParentDist gives the X-distance of the parent's axis from the child's axis. A positive value indicates the parent is in front of the child.  
  
Example:  
```  
trigger1 = ParentDist X != 0  
; Triggers if the parent is not at the exact same x-position as the  
  helper character.  
```

---

## ParentDist Z (changed)

The `ParentDist` trigger now also accepts a `Z` argument. Returns the distance between the helper and its parent in the Z axis.

---

## ParentExist (new)

Returns true if the helper's parent is still present in the game.

```
if parentExist {
    bindToParent{}
}
```

---

## PauseTime (new)

Returns the time until the active Pause and/or SuperPause effect expires (whichever lasts longer). The non 0 value is returned only after movetime parameter of these sctrls expires (player can no longer move).

Normally states are not running during Pause and SuperPause, so this trigger will only work when used in a special statedef -4, which ignores these state controllers.

>Format:  
>PauseTime  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = PauseTime = 0
  ;triggers when the player's movement is not paused by Pause/SuperPause sctrls.
```

---

## Physics (new)

Returns the player's physics-type. Refer to the section on StateDef in the CNS documentation for more details on physics.

>Format:  
>Physics [oper] physics_type  
>  
>Arguments:  
>[oper]  
>=, != (other operators not valid)  
>  
>physics_type (string)  
>S, C, A, N *(stand, crouch, air, none)*  
>  
>Return type:  
>boolean int (1 or 0)  

```ini
trigger1 = Physics != A
```

---

## Pi (math) (old)

This trigger returns the numeric value of pi (3.141593...)  
  
**Format:**  
pi  
  
**Arguments:**  
none  
  
**Return type:**  
float  
  
**Error conditions:**  
none

---

## PlayerIDExist (old)

Returns 1 if a player with the specified ID number exists, 0 otherwise. This ID number is obtained using the "ID" trigger (see ID). Do not confuse PlayerID with TargetID.  
  
**Format:**  
PlayerIDExist(ID_number)  
  
**Arguments:**  

**ID_number**  
An expression that evaluates to the ID number to check for (int)
  
  
**Return type:**  
boolean int (1 or 0)  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom.  
  
Example:  
```  
trigger1 = PlayerIDExist(var(4))  
; Triggers if a player with an ID number equal to the value of  
  var(4) exists.  
```

---

## PlayerIndexExist(n) (new)

Returns 1 if a player with the specified index number exists, 0 otherwise. See [PlayerIndex](Triggers-(new)/#redirection_playerindex).

```ini
trigger1 = PlayerIndexExist(2)
```

---

## PlayerNo (new)

Returns character's player number. Player 1 side uses odd numbers (1, 3, 5, 7), player 2 side even numbers (2, 4, 6, 8). Stage [AttachedChar](Stage-features/#info_attachedchar) uses number outside maximum player range (9).

>Format:  
>PlayerNo  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = PlayerNo < 3
```

---

## PlayerNoExist (new)

Evaluates if the specified player number is currently in use.  

>Format:  
>PlayerNoExist(player_number)  
>  
>Arguments:  
>player_number  
>An expression that evaluates to the player number to check for (int)  
>  
>Return type:  
>boolean int (1 or 0)  

Example:

```ini
trigger1 = PlayerNoExist(3); Returns true if there's a player number 3
trigger1 = Player(3), Alive
```

---

## Pos (old)

Gets the value of the player's position.  
You must specify the component that you want to check, eg. "Pos Y" to check the Y-position.  
  
**Format:**  
Pos [component]  
  
**Arguments:**  

**[component]**  
X, Y
  
  
**Return type:**  
float  
  
**Error conditions:**  
none  
  
**Details:**  
For "Pos X", the value is relative to the center of the screen (value 0). Negative is left, positive is right.  
Due to historical reasons, "Pos X" does not return absolute position of the player (i.e. relative to the center of the stage), which may be the more intuitive behavior.  
To get the absolute position of the player, use `Pos X + CameraPos X`.  
For "Pos Y", the value is relative to the floor. Negative is higher up, positive is below the floor.  
  
Example:  
```  
trigger1 = Pos Y >= 0  
; True when the player is below the floor.  
```

---

## Power (old)

Returns the amount of power the player has.  
  
**Format:**  
Power  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = power >= 1000  
  True if player has at least 1000 power (level 1).  
```

---

## PowerMax (old)

Returns the maximum amount of power the player can have. This is normally 3000 (level 3).  
  
**Format:**  
PowerMax  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = power < powermax / 2  
  True if player has less than half his maximum power.  
```

---

## PrevAnim (new)

Returns the number of the anim that the player was last in.

Example:

>Format:  
>PrevAnim  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = PrevAnim = 200
```

---

## PrevMoveType (new)

Returns the MoveType that the player was last in.

Example:

>Format:  
>PrevMoveType  
>  
>Arguments:  
>[oper]  
>=, != (other operators not valid)  
>  
>move_type (char)  
>move_type to compare against: A, I, H (Attack, Idle and GetHit move-types respectively) 
>  
>Return type:  
>boolean int (1 or 0)  

```ini
trigger1 = PrevMoveType = H
```

---

## PrevStateNo (old)

Returns the number of the state that the player was last in.  
The results of this trigger are not guaranteed to be accurate.  
  
**Format:**  
StateNo  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = PrevStateNo = [200,650]  
  Returns true if the player's last state number is between 200 and 650,  
  inclusive.  
```

---

## PrevStateType (new)

Returns the StateType that the player was last in.

Example:

>Format:  
>PrevStateType  
>  
>Arguments:  
>[oper]  
>=, != (other operators not valid)  
>  
>state_type (char)  
>state_type to compare against: S, C, A, L (Stand, Crouch, Air and Liedown respectively)
>  
>Return type:  
>boolean int (1 or 0)  

```ini
trigger1 = PrevStateType = C
```

---

## ProjCancelTime (old)

This trigger takes an required nonnegative ID number as an argument.  
If the player's last projectile to make any kind of contact was cancelled by an opponent's projectile and had the specified ID number, then ProjCancelTime returns the number of ticks since that contact occurred.  
If the specified ID number is 0, then the projectile ID is not checked.  
If no projectile meets all the above conditions, then ProjCancelTime returns -1.  
  
**Format:**  
ProjCancelTime(exprn)  
  
**Arguments:**  

**exprn**  
Expression evaluating to a nonnegative ID number (int).
  
  
**Return type:**  
int  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom. If a negative ID is  
specified, then the ID defaults to zero.  
  
Examples:  
```  
1. trigger1 = ProjCancelTime(1234) = 1  
; Triggers if a projectile with ID 1234 was just cancelled by an  
  opponent's projectile.  
2. trigger1 = ProjCancelTime(0) != -1 && ProjCancelTime(0) < 15  
; Triggers if any of the player's projectiles were cancelled  
  within last 15 ticks.  
```

---

## ProjClsnOverlap (new)

Returns true if the projectile's collision box (either clsn1 or clsn2) overlaps with another player's collision boxes.  
This trigger uses Ikemen's internal collision detection, so it will work even with angled and rescaled boxes.  
If you want to specify a projectile with a specific projID, create a loop process that combines the projID with ProjVar.  

>Format:  
>ProjClsnOverlap(index, playerID, box_type)
>  
>Arguments:  
>index  
>An index number based on all projectiles owned by the player.  
>The index is equivalent to the index when -1 is specified for the ID in ProjVar.  
>
>playerID  
>The ID of the player against which to check the overlap  
>  
>box_type  
>The target's collision box type. Valid values are clsn1, clsn2, and size  
>  
>Return type:  
>boolean int (1 or 0)  

```ini
trigger1 = ProjClsnOverlap(var(3), p2,ID, clsn2)
```

---

## ProjContact (old)

This trigger takes an optional ID number as a suffix.  
If the ID number is omitted, ProjContact returns true if any of the player's projectiles either successfully hit the opponent or were guarded by the opponent.  
When the ID number is specified, ProjContact returns true only if any of the player's projectiles with the specified ID number either successfully hit the opponent or was guarded.  
  
**Format:**  
- ProjContact[ID] = value  
- ProjContact[ID] = value, [oper] value2  
  
**Arguments:**  

**[ID]**  
Optional ID number.  
**value (boolean)**  
Value to compare against. 0 for false, 1 for true.  
**[oper]**  
=, !=, <, >, <=, >=  
**value2**  
Time value to compare against.
  
  
**Return type:**  
boolean int  
  
**Error conditions:**  
none  
  
**Details:**  
ProjContact will trigger once for each hit of the projectile, so a multi-hit projectile can trigger multiple times.  
The first form of ProjContact shown above is only valid for one tick after contact, unlike MoveContact.  
For the second form, ProjContact returns true if the projectile made contact n ticks ago, where n is a nonnegative number satisfying the relation "n [oper] value2".  
Specifying an ID number of 0 gives the same behavior as if the ID number is omitted (check all projectiles).  
  
  
Examples:  
```  
1. trigger1 = ProjContact1234 = 1  
; Triggers if a projectile with ID 1234 just made contact with the  
  opponent.  
2. trigger1 = ProjContact456 = 0, < 15  
; Triggers if no projectile with ID 456 made contact in the last 15  
  ticks.  
```

---

## ProjContactTime (old)

This trigger takes an required nonnegative ID number as an argument.  
If the player's last projectile to make any kind of contact, made contact with the opponent and had the specified ID number, then ProjContactTime returns the number of ticks since that contact occurred.  
If the specified ID number is 0, then the projectile ID is not checked.  
If no projectile meets all the above conditions, then ProjContactTime returns -1.  
  
**Format:**  
ProjContactTime(exprn)  
  
**Arguments:**  

**exprn**  
Expression evaluating to a nonnegative ID number (int).
  
  
**Return type:**  
int  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom.  
If a negative ID is specified, then the ID defaults to zero.  
  
Examples:  
```  
1. trigger1 = ProjContactTime(1234) = 1  
; Triggers if a projectile with ID 1234 just made contact with  
  the opponent.  
2. trigger1 = ProjContactTime(0) != -1 && ProjContactTime(0) < 15  
; Triggers if any of the player's projectiles made successful  
  contact with the opponent within the last 15 ticks.  
```

---

## ProjGuarded (old)

This trigger takes an optional ID number as a suffix.  
If the ID number is omitted, ProjGuarded returns true if any of the player's projectiles were guarded by the opponent.  
When the ID number is specified, ProjGuarded returns true only if one of the player's projectiles with the specified ID number was guarded by the opponent.  
  
**Format:**  
- ProjGuarded[ID] = value  
- ProjGuarded[ID] = value, [oper] value2  
  
**Arguments:**  

**[ID]**  
Optional ID number.  
**value (boolean)**  
Value to compare against. 0 for false, 1 for true.  
**[oper]**  
=, !=, <, >, <=, >=  
**value2**  
Time value to compare against.
  
  
**Return type:**  
boolean int (1 or 0)  
  
**Error conditions:**  
none  
  
**Details:**  
ProjGuarded will trigger once for each hit of the projectile, so a multi-hit projectile can trigger multiple times.  
The first form of ProjGuarded shown above is only valid for one tick after hit, unlike MoveGuarded.  
For the second form, ProjGuarded returns true if the projectile was guarded n ticks ago, where n is a nonnegative number satisfying the relation "n [oper] value2".  
Specifying an ID number of 0 gives the same behavior as if the ID number is omitted (check all projectiles).  
  
Examples:  
```  
1. trigger1 = ProjGuarded1234 = 1  
; Triggers if the opponent just blocked a projectile with ID 1234.  
2. trigger1 = ProjGuarded = 1, < 15  
; Triggers if the opponent blocked any projectile in the last 15  
  ticks.  
```

---

## ProjGuardedTime (old)

This trigger takes an required nonnegative ID number as an argument.  
If the player's last projectile to make any kind of contact was guarded by the opponent and had the specified ID number, then ProjGuardedTime returns the number of ticks since that contact occurred.  
If the specified ID number is 0, then the projectile ID is not checked.  
If no projectile meets all the above conditions, then ProjGuardedTime returns -1.  
  
**Format:**  
ProjCancelTime(exprn)  
  
**Arguments:**  

**exprn**  
Expression evaluating to a nonnegative ID number (int).
  
**Return type:**  
int  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom. If a negative ID is  
specified, then the ID defaults to zero.  
  
Examples:  
```  
1. trigger1 = ProjGuardedTime(1234) = 1  
; Triggers if a projectile with ID 1234 was just guarded by the  
  opponent.  
2. trigger1 = ProjGuardedTime(0) != -1 && ProjGuardedTime(0) < 15  
; Triggers if any of the player's projectiles was guarded by the  
  opponent within the last 15 ticks.  
```

---

## ProjHit (old)

This trigger takes an optional positive ID number as a suffix.  
If the ID number is omitted, ProjHit returns true if any of the player's projectiles successfully hit the opponent.  
When the ID number is specified, ProjHit returns true only if one of the player's projectiles with the specified ID number successfully hit the opponent.  
  
**Format:**  
- ProjHit[ID] = value  
- ProjHit[ID] = value, [oper] value2  
  
**Arguments:**  
*[ID] (int)*  
Optional ID number.  
*value (boolean)*  
Value to compare against. 0 for false, 1 for true.  
**[oper]*  
=, !=, <, >, <=, >=  
*value2*  
Time value to compare against.  
  
**Return type:**  
boolean int  
  
**Error conditions:**  
none  
  
**Details:**  
ProjHit will trigger once for each hit of the projectile, so a multi-hit projectile can trigger multiple times.  
The first form of ProjHit shown above is only valid for one tick after hit, unlike MoveHit.  
For the second form, ProjHit returns true if the projectile hit n ticks ago, where n is a nonnegative number satisfying the relation "n [oper] value2".  
Specifying an ID number of 0 gives the same behavior as if the ID number is omitted (check all projectiles).  
  
  
Examples:  
```  
1. trigger1 = ProjHit1234 = 1  
; Triggers if a projectile with ID 1234 just made successful contact with the opponent.  
2. trigger1 = ProjHit1234 = 1, < 15  
; Triggers if any of the player's projectiles made successful contact with the opponent within the last 15 ticks.  
```

---

## ProjHitTime (old)

This trigger takes an required nonnegative ID number as an argument.  
If the player's last projectile to make any kind of contact successfully hit the opponent and had the specified ID number, then ProjHit returns the number of ticks since that contact occurred.  
If the specified ID number is 0, then the projectile ID is not checked.  
If no projectile meets all the above conditions, then ProjHitTime returns -1.  
  
**Format:**  
ProjHitTime(exprn)  
  
**Arguments:**  
*exprn*  
Expression evaluating to a nonnegative ID number (int).
  
**Return type:**  
int  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom. If a negative ID is  
specified, then the ID defaults to zero.  
  
Examples:  
```  
1. trigger1 = ProjHitTime(1234) = 1  
; Triggers if a projectile with ID 1234 just made successful  
  contact with the opponent.  
2. trigger1 = ProjHitTime(0) != -1 && ProjHitTime(0) < 15  
; Triggers if any of the player's projectiles made successful  
  contact with the opponent within the last 15 ticks.  
```

---

## ProjVar (new)

Returns the specified projectile parameter. Use -1 for ID to iterate over all projectiles.

>Format:  
>ProjVar(id, index, param)  
>  
>Arguments:  
>id  
>Expression 1  
>  
>index  
>Expression 2  
>  
>param  
>Valid values are accel x, accel y, anim, animelem, angle, angle x, angle y, attr, drawpal group, drawpal index, guardflag, highbound, hitflag, layerno, lowbound, pausemovetime, pos x, pos y, projcancelanim, projedgebound, projhitanim, projhits, projID, projmisstime, projpriority, projremove, projremovetime, projremanim, projstagebound, remvelocity x, remvelocity y, scale x, scale y, shadow r, shadow g, shadow b, sprpriority, teamside, vel x, vel y, velmul x, velmul y  
>  
>Return type:  
>int or float  

Note:  
`attr`, `guardflag` and `hitflag` require a comparison against known flags.  

```ini
trigger1 = ProjVar(1000, 0, vel Y) > 0
trigger2 = ProjVar(2000, 0, attr) = SCA, HP
trigger3 = ProjVar(3000, 0, guardflag) = L
```

---

## Rad (Math) (new)

Converts an argument value from degree to radians.

>Format:  
>Rad(exp)  
>  
>Arguments:  
>exp  
>Expression  
>  
>Return type:  
>float  

```ini
trigger1 = Rad(Angle) > pi*0.5
```

---

## Random (old)

Returns a random number between 0 and 999, inclusive.  
  
**Format:**  
Random  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = Random <= 249  
; Triggers if the random number returned is less than or equal to  
  249. (This occurs with 25% probability.)  
```

---

## RandomRange(math) (new)

Generates pseudo-random integer numbers uniformly distributed between the given range (both bounds inclusive).  

>Format:  
>RandomRange(lower,upper)  
>  
>Arguments:  
>lower  
>Lower range (inclusive)  
>  
>upper  
>Upper range (inclusive)  
>  
>Return type:  
>int  

```ini
type = Explod
trigger1 = RandomRange(var(3), 666) > 100
pos = RandomRange(-300, 600), 0
```

---

## ReceivedDamage (new)

Returns the total damage dealt by the opposite team to this character, in the currently ongoing combo. This value is valid as long as the opposite team combo count stays above 0, otherwise it returns 0 too.

>Format:  
>ReceivedDamage  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = ReceivedDamage > (LifeMax / 10)
```

---

## ReceivedHits (new)

Returns the total number of hits done by the opposite team to this character, in the currently ongoing combo. Unlike GetHitVar(hitcount), it takes into account all hits, including those applied by HitAdd. This value is valid as long as the opposite team combo count stays above 0, otherwise it returns 0 too.

>Format:  
>ReceivedHits  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = ReceivedHits > 10
```

---

## RedLife (new)

Returns the amount of [red life](Miscellaneous-Info/#redlife) the player has.

>Format:  
>RedLife  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = RedLife = 0
```

---

## ReversalDefAttr (new)

Checks the attribute parameter of the player's currently-active ReversalDef. If the player does not currently have an active ReversalDef, then no parameters will match. Can be used for AI to detect a counter or to code something to happen if it exists.

Note: ReversalDefAttr != value1, value2 is logically equivalent to !(ReversalDefAttr = value1, value2).

>Format:  
>	ReversalDefAttr [oper] value1, value2  
>  
>Arguments:  
>	[oper]  
>=, !=  
>  
>	value1  
>A string that has at least one of the letters "S", "C" and "A" for standing, crouching and aerial attacks respectively. For example, "SA" is for standing and aerial attacks.  
>  
>	value2  
>A set of 2-character strings, separated by commas. Each 2-character string must be of the form described: The first character is either "N" for "normal", "S" for "special", or "H" for "hyper". The second character must be either "A" for "attack" (a normal hit attack) or "T" for "throw". For example, "NA, ST" is for normal attacks and special throws.  
>  
>Assuming the attribute of the player's ReversalDefAttr is in the form:  
>  
>arg1, arg2  
>  
>then the trigger condition is determined to be true only if arg1 is a subset of value1, AND arg2 is a subset of value2.  
>  
>Return type:  
>	boolean int (1 or 0)  
>  
>Error conditions:  
>	none  

Example:

```ini
trigger1 = ReversalDefAttr = A, HA
  Triggers when the player activates a ReversalDef with the following attributes:  
    1. player will reverse an aerial attack
    2. player will reverse a hyper (super) attack

trigger1 = ReversalDefAttr = SC, NA, SA
  Triggers when the player activates a ReversalDef with the following attributes:
    1. player will reverse both standing and crouching attacks
    2. player will reverse both normal and special attacks
```

---

## RightEdge (old)

RightEdge returns the x position of the right edge of the screen, in absolute stage coordinates.  
  
**Format:**  
LeftEdge  
  
**Arguments:**  
none  
  
**Return type:**  
float  
  
**Error conditions:**  
none  
  
**Notes:**  
This trigger is equivalent to the expression `CameraPos X + GameWidth / 2`.  
  
Example:  
```  
trigger1 = Pos X + CameraPos X > RightEdge  
; Triggers if the player is to the right of the right edge of the screen.  
```

---

## RootDist (old)

This trigger is only valid for helper-type characters.  
RootDist returns the distance from the helper to its root.  
The root is the main player character who owns the helper: for instance, if you select Kumquat to play with, and Kumquat spawns a helper named Kiwi, who in turn spawns a helper named Penguin, then Penguin's root is Kumquat, and Penguin is a descendant of Kumquat.  
RootDist works similarly to P2Dist.  
  
**Format:**  
RootDist [component]  
  
**Arguments:**  

**[component]**  
X, Y
  
**Return type:**  
float  
  
**Error conditions:**  
Returns bottom if the player has no root.  
  
**Details:**  
For comparing the Y-distance, RootDist gives the difference in the heights of the players' Y-axes. A negative value means that the root is above its descendant.  
For comparing the X-distance, ParentDist gives the X-distance of the root's axis from the descendant's axis. A positive value indicates the root is in front of its descendant.  
  
Example:  
```  
trigger1 = RootDist X != 0  
; Triggers if the root is not at the exact same x-position as the helper character.  
```

---

## RootDist Z (changed)

The `RootDist` trigger now also accepts a `Z` argument. Returns the distance between the helper and its root in the Z axis.

---

## Round (math) (new)

Returns the rounded value of `val` to specified `precision` (number of digits after the decimal point). `precision` can also be negative or zero.

>Format:  
>Round(val,precision)  
>  
>Arguments:  
>val  
>Expression evaluating to the value to round.  
>  
>precision  
>Expression evaluating to the number of decimal digits to round to. If the precision is positive, the rounding will occur after the decimal point. If the precision is negative, the rounding will occur before the decimal point. If the absolute value of the precision is greater than or equal to the number of digits, the result of the rounding is equal to 0.  
>  
>Return type:  
>float  

```ini
trigger1 = Round(var(3), -2) > 100
```
```ini
trigger1 = Round(1.0055, 3) ; returns 1.006
```

---

## RoundNo (old)

Returns the current round number.  
  
**Format:**  
RoundNo  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = RoundNo = 3  
; Triggers if this is the third round of the match.  
```

---

## RoundsExisted (old)

Returns the number of rounds the player has existed for. On the first round, returns 0.  
This is useful for a Turns mode intro.  
  
**Format:**  
RoundsExisted  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = RoundsExisted = 0  
trigger1 = TeamMode = Turns  
trigger1 = RoundNo > 0  
; Triggers if the player has just entered a Turns mode team match  
  after the first round. You can use this example with a  
  ChangeState controller to switch to an intro state by  
  overriding the Initialize state (state 5900).  
```

---

## RoundState (old)

Returns the current round state number.  
  
**Format:**  
RoundState  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
**Details:**  
Return values:  
0: Pre-intro  - screen fades in  
1: Intro  
2: Fight - players do battle  
3: Pre-over - just a round is won or lost  
4: Over - win poses  
  
Example:  
```  
trigger1 = RoundState = 2  
; Triggers if the actual fighting portion of the round is in  
  progress.  
```

---

## RoundState (changed)

The `RoundState` trigger no longer returns 2 during the "Fight!" screen, before players have control, returning 1 instead.  
`RoundState = 2` is generally understood and documented as the main part of the fight, so this oddity only caused trouble in Mugen.

---

## RoundsWon (new)

Returns how many total rounds the teamside has won during the current match. Resets between matches.

[TODO]

---

## RoundTime (new)

Returns the tick count since the start of the round.

>Format:  
>RoundTime  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = RoundTime > 600
```

---

## RunOrder (new)

At the start of each frame, players are sorted into a list for code processing based on their current actions (see [character processing order](Miscellaneous-info#character-processing-order)). `RunOrder` returns their position in this list as an integer.

---

## Scale (new)

Returns the value of the player's drawing scale. `Scale X` and `Scale Y` refer to the scale applied by `AngleDraw`. `Scale Z` refers to the rescaling that affects the player when moving in the Z space.  

>Format:  
>Scale argument
>  
>Arguments:  
>x, y, z
>  
>Return type:
>float

```ini
trigger1 = Scale x > 2 && Scale y > 1
```

---

## Score (new)

Returns the score points gained in this round by all team members.

>Format:  
>Score  
>  
>Arguments:  
>none  
>  
>Return type:  
>float  

```ini
trigger1 = Score > 10000
```

---

## ScoreTotal (new)

Returns the total score points value. Takes into account all team members, previous rounds and previous matches since the start of this game mode.

>Format:  
>ScoreTotal  
>  
>Arguments:  
>none  
>  
>Return type:  
>float  

```ini
trigger1 = ScoreTotal > 1000000
```

---

## ScreenHeight (old)

Returns the height of the screen space in the player's local coordinate space.  
  
**Format:**  
ScreenHeight  
  
**Arguments:**  
none  
  
**Return type:**  
float  
  
**Error conditions:**  
none  
  
**Notes:**  
ScreenWidth and ScreenHeight are not affected by the camera zoom factor.  
  
Example:  
```  
type = Explod  
space = screen  
pos = 0, ScreenHeight  
...  
  Creates an explod in screen-space in the lower-right corner  
  of the screen.  
```

---

## ScreenPos (old)

Gets the value of the player's position relative to the top-right corner of the screen.  
  
**Format:**  
ScreenPos [component]  
  
**Arguments:**  

**[component]**  
X, Y
  
  
**Return type:**  
float  
  
**Error conditions:**  
none  
  
**Details:**  
For `ScreenPos X`, the value is relative to the left of the screen (value 0). Negative is left, positive is right.  
For `ScreenPos Y`, the value is relative to the top of the screen. Negative is above the screen, positive is downward.  
  
  
Example:  
```  
trigger1 = ScreenPos Y >= 0 && ScreenPos Y < GameHeight  
; True when the player's is in the screen's vertical extent.  
```

---

## ScreenWidth (old)

Returns the width of the screen space in the player's local coordinate space.  
  
**Format:**  
ScreenWidth  
  
**Arguments:**  
none  
  
**Return type:**  
float  
  
**Error conditions:**  
none  
  
**Notes:**  
ScreenWidth and ScreenHeight are not affected by the camera zoom factor.  
  
Example:  
```  
type = Explod  
space = screen  
pos = ScreenWidth / 2, ScreenHeight / 2  
...  
  Creates an explod in screen-space in the center of the screen.  
```

---

## SelfAnimExist (old)

Like AnimExist, except that this only checks P1's animation data.  
If P1 has been given P2's animation data by a hit, SelfAnimExist will not check P2's animation data to determine whether or not a given action exists.

---

## SelfCommand (new)

[TODO]

---

## SelfStatenoExist (new)

Checks for the existence of a state only within P1's state numbers, even when P1 is custom stated by a hit. Returns 1 if there is a statedef with the specified number. Otherwise it returns 0. Use the statedef number you want to recognize in parentheses.

>Format:  
>SelfStatenoExist(exprn)  
>  
>Arguments:  
>exprn  
>An expression evaluating to a state number (int).  
>  
>Return type:  
>boolean int (1 or 0)  

```ini
trigger1 = !SelfStatenoExist(200)
  ;Triggers if the player is missing state 200.
```

---

## Sign (Math) (new)

Returns the sign of a real number. If value < 0 return -1. If value 0 return 0. if value > 0 return 1.

>Format:  
>Sign(exp)
>  
>Arguments:  
>exp  
>Expression  
>  
>Return type:  
>int

```ini
var(0) = var(0)*Sign(vel x)
```

---

## Sin (math) (old)

Computes the sine of the specified argument (in radians.)  
  
**Format:**  
sin(exprn)  
  
**Arguments:**  

**exprn**  
Expression to compute the sine of. (float)
  
  
**Return type:**  
float  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom.  
  
Example:  
```  
value = sin(pi/2)  
; Sets value to the sine of pi/2, which is approximately 1.0 (possibly with some rounding error.)  
```

---

## SoundVar (new)

Returns the specified sound channel parameter. Use -1 for channelNo to find the first sound available.

**Warning: The results of this trigger are NOT network-safe due to the asynchronous nature of sound playback. Usage of this trigger in production environments is discouraged.**

>Format:  
>SoundVar(channelNo, param)  
>  
>Arguments:  
>channelNo  
>Expression  
>  
>param  
>Valid values are group, number, freqmul, isplaying, length, loopcount, loopstart, loopend, pan, position, priority, startposition, volumescale  
>  
>Return type:  
>int or float  

```ini
var(0) = SoundVar(0, IsPlaying)
fvar(1) = SoundVar(1, VolumeScale)
```

---

## SpriteVar (new)

Returns information about the player's current sprite.  

>Format:  
>SpriteVar(param_name)  
>  
>Arguments:  
>param_name  
>The name of the parameter to check. Valid values are:  
>Group, Height, Image, Width, XOffset, YOffset

```ini
; top left corner of sprite
pos = -SpriteVar(xoffset), -SpriteVar(yoffset)
; lower right corner of sprite
pos = -SpriteVar(xoffset) + SpriteVar(width), -SpriteVar(yoffset) + SpriteVar(height)
```

---

## SprPriority (new)

Returns the player's/helper's current SprPriority value.

>Format:  
>SprPriority  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = SprPriority > 0
```

---

## StageBackEdgeDist (new)

Returns the distance to the stage edge (corner) behind the player.

>Format:  
>StageBackEdgeDist  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = StageBackEdgeDist < 100
```

---

## StageBGVar (new)

Returns information about the stage's BG elements.  

>Format:  
>stagebgvar(ID, index, param)
>  
>Arguments:  
>ID  
>The ID of the element to be checked  
>  
>index  
>The index of the element to be checked  
>  
>param  
>The parameter to check. See details  
>  
>Return type:  
>Varies. See details  

Details:
* `actionno`: Returns the animation number for `type = anim` elements (int)
* `delta.x`: Returns the X delta (float)
* `delta.y`: Returns the Y delta (float)
* `id`: Returns the ID (int)
* `layerno`: Returns the layer number (int)
* `pos.x`: Returns the X position in relation to the starting position (float)
* `pos.y`: Returns the Y position in relation to the starting position (float)
* `start.x`: Returns the X starting position (float)
* `start.y`: Returns the Y starting position (float)
* `tile.x`: Returns the X tiling flag (bool)
* `tile.y`: Returns the Y tiling flag (bool)
* `velocity.x`: Returns the X velocity (float)
* `velocity.y`: Returns the Y velocity (float)

Example:  
```ini
trigger1 = StageBGVar(4, 1, actionno) = 40
```

---

## StageConst (new)

Returns the value of one of the stage's constants. Stage constant variables can be set under stage's DEF [[Constants]](Stage-features/#constants) section.

>Format:  
>StageConst(param_name)  
>  
>Arguments:  
>param_name  
>The name of the constant to check (string).  
>  
>Return type:  
>float  

```ini
trigger1 = StageConst(WaterGround) = 1
```

---

## StageFrontEdgeDist (new)

Returns the distance to the stage edge (corner) in front of the player.

>Format:  
>StageFrontEdgeDist  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = StageFrontEdgeDist < 100
```

---

## StageTime (new)

Returns the stage's internal time, or the amount of ticks since the last stage reset. The value returned by this trigger corresponds directly to the amount of times stage backgrounds have been updated (taking into account `pausebg`, `resetbg`, etc), allowing one to for instance reliably synchronize [attachedchar](Stage-features/#info_attachedchar) actions to what's currently displayed by the stage.

>Format:  
>StageTime  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = StageTime > 600
```

---

## StageVar (old)

Returns information about the stage.  
A limited number of parameters are supported.  
  
**Format:**  
StageVar(param_name) [oper] "string"  
  
**Arguments:**  

**param_name**  

**The name of the stage parameter to check. Valid values are:**  
info.name, info.displayname, info.authorname.
  
**[oper]**  
=, != (other operators not valid)  
**"string" (string)**  
String to compare against. Must be in double quotes.
  
  
**Return type:**  
boolean int (1 or 0)  
  
**Error conditions:**  
none  
  
**Details:**  
- info.author: Compares the value of the "author" parameter in the `[Info]` group. (boolean)  
- info.displayname: Compares the value of the "displayname" parameter in the `[Info]` group. (boolean)  
- info.name: Compares the value of the "name" parameter in the `[Info]` group. (boolean)  
  
**Versions:**  
1.0 and newer  
  
Example:  
```  
trigger1 = StageVar(info.author) = "Suika"  
  Returns true if the stage author is named "Suika".  
```

---

## StageVar (changed)

StageVar now accepts all stage parameters that [ModifyStageVar](State-controllers-(new)/#new_modifystagevar) state controller can change. In addition it accepts the following parameters (nightly build only):

>info.ikemenversion = *version* (float)  
>info.mugenversion = *version* (float)  
>stageinfo.localcoord.x = *width* (int)  
>stageinfo.localcoord.y = *height* (int)

---

## Standby (new)

Returns 1 if character is under standby effect (assigned by [TagOut](State-controllers-(new)/#new_tagout) sctrl).

>Format:  
>Standby  
>  
>Arguments:  
>none  
>  
>Return type:  
>boolean int (1 or 0)  

```ini
trigger1 = !Standby
```

---

## StateNo (old)

Returns the player's current state number. Useful for "move interrupts" in the CMD file.  
  
**Format:**  
StateNo  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = stateno = [200,650]  
  Returns true if the state number is between 200 and 650,  
  inclusive.  
```

---

## StateType (old)

StateType gives the player's state-type. Refer to the section on StateDef in the CNS documentation for more details on StateType.  
Useful for "move interrupts" in the CMD file.  
  
**Format:**  
StateType [oper] state_type  
  
**Arguments:**  

**[oper]**  
=, !=   (other operators not valid)  
**state_type (char)**  

**S, C, A, L**  
Stand, Crouch, Air and Liedown state-types.
  
**Return type:**  
boolean int (1 or 0)  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = StateType != A  
; Triggers if the player is not in an air-type state.  
```

---

## SysFVar (old)

This trigger takes a mandatory variable number as an argument. It returns the value of the player's specified system float variable.  
This trigger should NOT be used under normal circumstances. System  
variables are reserved for bookkeeping in common1.cns.  
  
**Format:**  
SysFVar(exprn)  
  
**Arguments:**  

**exprn**  
An expression evaluating to a variable number. Valid numbers  
at this time are 0-4.
  
**Return type:**  
float  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom, or if exprn evaluates  
to an invalid variable index.  
  
Example:  
```  
trigger1 = SysFVar(0) = -1.23  
; Triggers if the value of system float variable 0 is -1.23.  
```

---

## SysVar (old)

This trigger takes a mandatory variable number as an argument. It returns the value of the player's specified system int variable.  
This trigger is NOT to be used under normal circumstances. System  
variables are reserved for bookkeeping in common1.cns.  
  
**Format:**  
SysVar(exprn)  
  
**Arguments:**  

**exprn**  
An expression evaluating to a variable number. Valid numbers  
at this time are 0-4.
  
  
**Return type:**  
int  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom, or if exprn evaluates  
to an invalid variable index.  
  
Example:  
```  
trigger1 = SysVar(0) = -34  
; Triggers if the value of system variable 0 is -34.  
```

---

## Tan (math) (old)

Computes the tangent of the specified argument (in radians.)  
  
**Format:**  
tan(exprn)  
  
**Arguments:**  

**exprn**  
Expression to compute the tangent of. (float)
  
  
**Return type:**  
float  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom.  
  
Example:  
```  
value = tan(pi/4)  
  Sets value to the tangent of pi/4, which is approximately 1.0  
  (possibly with some rounding error.)  
```

---

## TeamLeader (new)

Returns [playerno](Triggers-(new)/#playerno) of the character that is considered a team leader. In modes where only one player is controlled in particular round (*single*, *turns* and *ratio*) it will be either 1 or 2, depending on team side. In *simul* and *tag* modes, team leader is the first party member (again 1 or 2) by default, but who is considered a leader can be also dynamically adjusted via optional [TagIn](State-controllers-(new)/#new_tagin) sctrl *leader* parameter.

Manually swapping leader changes lifebar elements assignment - leader always uses P1 (or P2, depending on team side) lifebar elements, remaining players positions are moved accordingly, in ascending players order.

>Format:  
>TeamLeader  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = TeamLeader = PlayerNo
```

---

## TeamMode (old)

TeamMode gives the current mode of play for the player's team.  
  
**Format:**  
TeamMode [oper] mode  
  
**Arguments:**  
*[oper]*  
=, !=   (other operators not valid)  
*mode (string)*  
single - single player
simul  - 2 players simultaneously
turns  - turns battle
  
**Return type:**  
boolean int (1 or 0)  
  
**Error conditions:**  
none  
  
**Notes:**  
In survival mode, TeamMode = turns on the enemy side.  
  
Example:  
```  
trigger1 = TeamMode = Single  
; Triggers if the player is playing in single play.  
```

---

## TeamMode = Tag (changed)

Now TeamMode can also return "Tag".

Note that TeamMode returns "Turns" during Ratio mode.

```ini
trigger1 = TeamMode = Tag
```

---

## TeamSide (old)

Returns the team side the player is on. 1 represents P1 side (left), 2 for P2 side (right).  
  
**Format:**  
TeamSide  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = TeamSide = 2  
; Triggers if player is on the P2 side team.  
```

---

## TeamSize (new)

Returns character's team size (for *turns* mode it returns information that was previously not obtainable, for other team modes the returned value is equivalent to using `NumPartner + 1`)

>Format:  
>TeamSize  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = TeamSize = 4
```

---

## TicksPerSecond (old)

Returns the number of ticks per second. Useful for time calculations.  
  
**Format:**  
TicksPerSecond  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = Time > 10 * TicksPerSecond  
; Triggers after 10 seconds, regardless of game speed.  
```

---

## Time (old)

Returns the state-time of the player (that is, the number of ticks that the player has been in the current state so far).  
  
**Format:**  
Time  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = Time = 2  
; Triggers when the player's state-time is 2.  
```

---

## TimeElapsed (new)

Returns the amount of clock ticks since the battle began (0 if time is disabled). Value returned by this trigger corresponds to lifebar timer (only ticks during RoundState = 2)

>Format:  
>TimeElapsed  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = TimeElapsed > 600
```

---

## TimeMod (old)

Returns the remainder when the state-time of the player is divided by the specified value.  
The `%` operator subsumes the functionality of `TimeMod`, so it is recommended that you use `%` instead.  
  
**Format:**  
TimeMod [oper] divisor, value1  
  
**Arguments:**  
*[oper]*  
=, !=, <, >, <=, >=  
*divisor (int)*  
Positive number to use as a divisor.  
*value1 (int)*  
Value to compare remainder against.
  
  
**Return type:**  
boolean int (1 or 0)  
  
**Error conditions:**  
Returns bottom if the divisor is 0.  
  
Example:  
```  
trigger1 = TimeMod = 4, 3  
; Triggers when the state-time is 3, 7, 11, 15, ...  
```

---

## TimeRemaining (new)

Returns the amount of clock ticks until time over (-1 if time is disabled). Value returned by this trigger corresponds to lifebar timer (only ticks during RoundState = 2)

>Format:  
>TimeRemaining  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = TimeRemaining > 600
```

---

## TimeTotal (new)

Returns the total number of clock ticks that have elapsed so far. Takes into account previous rounds and matches since the start of this game mode.

>Format:  
>TimeTotal  
>  
>Arguments:  
>none  
>  
>Return type:  
>int  

```ini
trigger1 = TimeTotal > 5940
```

---

## TopBoundBodyDist (new)

Like `TopBoundDist`, except this trigger accounts for the player's top `edge` parameter, as defined by the `Depth` state controller.

---

## TopBoundDist (new)

TopBoundDist gives the distance between the player's z-axis and the `topbound` limit of the stage.

>Format:  
>TopBoundDist 
>  
>Arguments:  
>none  
>  
>Return type:  
>float

```ini
trigger1 = TopBoundDist < 40
```

---

## TopEdge (old)

TopEdge returns the y position of the top edge of the screen, in absolute stage coordinates.  
  
**Format:**  
TopEdge  
  
**Arguments:**  
none  
  
**Return type:**  
float  
  
**Error conditions:**  
none  
  
**Notes:**  
This trigger is equivalent to the expression "Pos Y - ScreenPos Y".  
  
Example:  
```  
trigger1 = Pos Y > TopEdge  
; Triggers if the player is below the top edge of the screen.  
```

---

## UniqHitCount (old)

Returns the total number of hits the player's current attack move has done.  
This value is valid only for a single state; after any state change, it resets to 0.  
To prevent it from resetting to 0, set hitcountpersist in the StateDef (see cns documentation for details).  
The HitCount and UniqHitCount triggers differ only when the player is hitting more than one opponent.  
In the case where the player is hitting two opponents with the same attack, HitCount will increase by 1 for every hit, while UniqHitCount increases by 2.  
  
**Format:**  
UniqHitCount  
  
**Arguments:**  
none  
  
**Return type:**  
int  
  
**Error conditions:**  
none  
  
Example:  
```  
trigger1 = UniqHitCount = [4,6]  
; Triggers when 4, 5 or 6 hits have been dealt since the start of the player's attack move.  
```

---

## Var (old)

This trigger takes a mandatory variable number as an argument. It returns the value of the player's specified int variable.  
  
**Format:**  
Var(exprn)  
  
**Arguments:**  

**exprn**  
An expression evaluating to a variable number. Valid numbers at this time are 0-59.
  
  
**Return type:**  
int  
  
**Error conditions:**  
Returns bottom if exprn evaluates to bottom, or if exprn evaluates to an invalid variable index.  
  
Example:  
```  
trigger1 = Var(0) = -34  
; Triggers if the value of variable 0 is -34.  
```

---

## Vel (old)

Gets the value of the player's velocity. You must specify the component that you want to check, eg. `Vel Y` to check the Y-velocity.  
  
**Format:**  
Vel [component]  
  
**Arguments:**  

**[component]**  
X, Y
  
  
**Return type:**  
float  
  
**Error conditions:**  
none  
  
**Details:**  
For Vel X, a positive value indicates that the player is moving forward. (This behavior is the opposite of HitVel X's behavior.)  
For Vel Y, a positive value indicates that the player is moving downward.  
  
Example:  
```  
trigger1 = Vel Y >= 0  
; True when the player is not moving upward.  
```

---

## Win (old)

Returns true if the player (or the player's team, in team mode) has won the round, false otherwise.  
Can be suffixed with "KO", "Time", or "Perfect" to return true only when the round has been won by a KO, by time expiring, or with no life lost, respectively.  
  
Format:  
1. Win  
2. WinKO  
3. WinTime  
4. WinPerfect  
  
**Arguments:**  
none  
  
**Return type:**  
boolean int (1 or 0)  
  
**Error conditions:**  
none  
  
Examples:  
```  
trigger1 = Win  
; Triggers if the player (or his team) has won the round.  
  
trigger1 = !WinKO  
; Triggers if the player (or his team) has not won the round by a KO. For example, this will trigger if the player's team has not yet won the round, or if they have won the round by time over.  
```

---

## WinClutch (new)

Returns true if the player (or the player's team, in team mode) has won the round with health below the limit set by ``clutch.threshold`` in fight.def. If the parameter isn't defined, the default is under 10%.

>Format:  
>WinClutch  
>  
>Arguments:  
>none  
>  
>Return type:  
>boolean int (1 or 0)

---

## WinHyper (new)

Returns true if the player (or the player's team, in team mode) has won the round with the finishing blow being a hyper attack.

>Format:  
>WinHyper  
>  
>Arguments:  
>none  
>  
>Return type:  
>boolean int (1 or 0)  

```ini
trigger1 = !WinHyper
```

---

## WinSpecial (new)

Returns true if the player (or the player's team, in team mode) has won the round with the finishing blow being a special attack.

>Format:  
>WinSpecial  
>  
>Arguments:  
>none  
>  
>Return type:  
>boolean int (1 or 0)  

```ini
trigger1 = !WinSpecial
```

---

## XAngle (new)

Returns the value of the player's Xangle applied with AngleDraw/AngleSet/AngleAdd/AngleMul sctrl.

>Format:  
>XAngle
>  
>Arguments:  
>none  
>  
>Return type:
>float

```ini
trigger1 = XAngle >= 90
```

---

## Xshear (new)

Returns the value of the player's xshear applied with TransformSprite sctrl.

>Format:  
>xshear 
>  
>Arguments:  
>none  
>  
>Return type:  
>float

```ini
trigger1 = xshear > 40
```

---

## YAngle (new)

Returns the value of the player's yangle applied with AngleDraw/AngleSet/AngleAdd/AngleMul sctrl.

>Format:  
>YAngle
>  
>Arguments:  
>none  
>  
>Return type:
>float

```ini
trigger1 = YAngle >= 90
```

---

## ZoomVar (new)

Allows checking the scale, pos x, pos y, lag, and remaining time of the currently Zoom sctrl.

>Format:  
>ZoomVar(param_name)
>  
>Arguments:  
>param_name  
>The name of the variable to check. Valid values are:  
>scale, pos.x, pos.y, lag, time  
>  
>Return type:  
>int or float

```ini
trigger1 = ZoomVar(scale) < 0.9
trigger2 = ZoomVar(pos.x) >= 100

```

---

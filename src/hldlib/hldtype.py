from enum import Enum


class HLDType(str, Enum):
    """
    This enum contains all the possible object types in HLD. Collected from all levels and from data.win.
    """

    def __str__(self):
        return self.value

    MASTERCLASS = 'MasterClass'
    DOORSTOVISIT = 'doorsToVisit'
    PAUSEDELAYOBJ = 'PauseDelayObj'
    STUCKBOX = 'StuckBox'
    BATTERYCHARGER = 'BatteryCharger'
    BGSCENERY = 'BGScenery'
    BULLET = 'bullet'
    BURSTSHOT = 'BurstShot'
    CONFIRMWINDOW = 'ConfirmWindow'
    DECOR = 'Decor'
    DECORSHADOW = 'DecorShadow'
    DECORXRAYSHADOWBLOCK = 'DecorXRayShadowBlock'
    ENEMY = 'enemy'
    ENEMYHITMASK = 'EnemyHitMask'
    GAMEEXITER = 'GameExiter'
    HAZARD = 'Hazard'
    JUMPLEDGE = 'jumpledge'
    MANTLEABLE = 'Mantleable'
    MOVINGBLOCK = 'MovingBlock'
    OBJWINDOW = 'ObjWindow'
    PARTICLE = 'Particle'
    PATHFINDOBSTACLE = 'PathFindObstacle'
    PROJECTILEBLOCKCOLLIDER = 'ProjectileBlockCollider'
    SCENERY = 'Scenery'
    SIMPLEEFFECT = 'SimpleEffect'
    SIMPLEEFFECTGUI = 'SimpleEffectGUI'
    STATESCENERY = 'StateScenery'
    RECESSINGSCENERY = 'RecessingScenery'
    TIMELIMIT = 'TimeLimit'
    MENUS = 'Menus'
    CREDITS = 'Credits'
    TITLEHLD = 'titleHLD'
    PAXCHALLENGERESULTS = 'PAXChallengeResults'
    THANKYOUSCREEN = 'ThankYouScreen'
    TITLESCREEN = 'titlescreen'
    WAITER = 'Waiter'
    BOSSRUSHLEADERBOARDSAVER = 'BossRushLeaderboardSaver'
    EDITOROBJ = 'EditorObj'
    SPAWNER = 'Spawner'
    LEVELBOUNDARY = 'LevelBoundary'
    HOARDE = 'Hoarde'
    CHARMAKER = 'charmaker'
    CHARVICTORY = 'CharVictory'
    NEWREGIONSOUNDEVENT = 'NewRegionSoundEvent'
    ALLHOARDESBEATEN = 'AllHoardesBeaten'
    BONUSHOARDEBEATEN = 'BonusHoardeBeaten'
    DOOR = 'door'
    TITLEDOOR = 'TitleDoor'
    EDITORCHECKPOINT = 'EditorCheckpoint'
    REGION = 'Region'
    REGIONWALL = 'RegionWall'
    BOSSWALL = 'BossWall'
    BOOMBOX = 'BoomBox'
    AMBIENCE = 'Ambience'
    CAMERACUE = 'CameraCue'
    CAMERALOCK = 'CameraLock'
    CASERESETTER = 'CaseResetter'
    EMPTYOBJECT = 'EmptyObject'
    TRUEATINTERVAL = 'TrueAtInterval'
    PERMASTATE = 'PermaState'
    COLLECTIBLECHECK = 'CollectibleCheck'
    PLAYERHASMAPCHECK = 'PlayerHasMapCheck'
    WELLCHECK = 'WellCheck'
    ROOMVISITED = 'RoomVisited'
    BOSSCHECK = 'BossCheck'
    ONETIMETRUE = 'OneTimeTrue'
    PARALLAXOBJ = 'ParallaxObj'
    NOCOMBAT = 'NoCombat'
    NOSHOOT = 'NoShoot'
    NOWARP = 'NoWarp'
    EDITORBLOOMER = 'EditorBloomer'
    EDITORSCREENSHAKE = 'EditorScreenShake'
    EDITORSOUND = 'EditorSound'
    EDITORCUTSCENE = 'EditorCutscene'
    TUTORIALBUTTONPROMPT = 'TutorialButtonPrompt'
    TUTORIALINFINITESLIME = 'TutorialInfiniteSlime'
    EDITORWAYPOINT = 'EditorWaypoint'
    NOTE = 'Note'
    SPECIALWAYPOINT = 'SpecialWayPoint'
    DRIFTERDEATH = 'DrifterDeath'
    GLOWINGEYES = 'GlowingEyes'
    BLOODSPRAYER = 'BloodSprayer'
    ENEMYHPCHECKER = 'EnemyHPChecker'
    BOSSRUSH = 'BossRush'
    BOSSRUSHCHECKPOINT = 'BossRushCheckpoint'
    BOSSRUSHBOSSCHECK = 'BossRushBossCheck'
    AMBIENTSOUND = 'AmbientSound'
    GAUNTLETDOOR = 'GauntletDoor'
    CRISSCROSS = 'CrissCross'
    OVERTRIGGER = 'OverTrigger'
    UNDERTRIGGER = 'UnderTrigger'
    DOORBOTTOM = 'doorbottom'
    GRASS = 'grass'
    HALSPAWNER = 'HalSpawner'
    MIDDOOR = 'middoor'
    PUDDLE = 'puddle'
    DESTRUCTABLE = 'destructable'
    PHASECRYSTALMAKER = 'PhaseCrystalMaker'
    CRYSTALDESTRUCTABLE = 'CrystalDestructable'
    MULTIHITCRYSTAL = 'MultiHitCrystal'
    ORGANTUBETINY = 'OrganTubeTiny'
    ORGANTUBETHIN = 'OrganTubeThin'
    ORGANTUBESMALL = 'OrganTubeSmall'
    COLLECTIBLE = 'Collectible'
    COLLECTIBLECOLUMN = 'CollectibleColumn'
    CRATE = 'Crate'
    CRATEBIG = 'CrateBig'
    MULTIHITCRATE = 'MultiHitCrate'
    BARREL = 'Barrel'
    EXPLODINGBARREL = 'ExplodingBarrel'
    GEARBITCRATE = 'GearbitCrate'
    GEARBIT = 'Gearbit'
    MAP = 'Map'
    HEALTHKIT = 'HealthKit'
    DRIFTERBONES_KEY = 'DrifterBones_Key'
    DRIFTERBONES_WEAPON = 'DrifterBones_Weapon'
    DRIFTERBONES_OUTFIT = 'DrifterBones_Outfit'
    MODULESOCKET = 'ModuleSocket'
    LIBRARIANTABLET = 'LibrarianTablet'
    LIBRARYCASE = 'LibraryCase'
    LIBRARYWALL = 'LibraryWall'
    LIBRARYWALLFINAL = 'LibraryWallFinal'
    DRIFTERBONES = 'DrifterBones'
    BATTERYREFILLER = 'BatteryRefiller'
    HEALTHPLANT = 'HealthPlant'
    BUTTON = 'Button'
    BOSSRUSHLEADERBOARD = 'BossRushLeaderboard'
    HIGHSCOREBOARD = 'HighScoreBoard'
    SMALLHIGHSCOREBOARD = 'SmallHighScoreBoard'
    TOGGLESWITCH = 'ToggleSwitch'
    RAILGUNSWITCH = 'RailgunSwitch'
    TERMINAL = 'Terminal'
    WARPPAD = 'WarpPad'
    STAIRSRIGHT = 'StairsRight'
    STAIRSLEFT = 'StairsLeft'
    SMALLSTAIRSRIGHT = 'SmallStairsRight'
    SMALLSTAIRSLEFT = 'SmallStairsLeft'
    STAIRSUP = 'StairsUp'
    SMALLSTAIRSUP = 'SmallStairsUp'
    JUMPPAD = 'JumpPad'
    INVISIBLEPLATFORM = 'InvisiblePlatform'
    LIGHT = 'Light'
    ROOMDOOR = 'RoomDoor'
    DIAMONDDOOR = 'DiamondDoor'
    VANISHINGDOOR = 'VanishingDoor'
    TELEVATOR = 'Televator'
    BIGBOSSDOOR = 'BigBossDoor'
    DRIFTERVAULTDOOR = 'DrifterVaultDoor'
    MODULEDOOR = 'ModuleDoor'
    SHORTWARP = 'ShortWarp'
    TELEPORTER = 'Teleporter'
    UPGRADESWORD = 'UpgradeSword'
    UPGRADEDASH = 'UpgradeDash'
    UPGRADEHEALTHPACK = 'UpgradeHealthPack'
    UPGRADESPECIAL = 'UpgradeSpecial'
    UPGRADEWEAPON = 'UpgradeWeapon'
    APARTMENTDIAGRAM = 'ApartmentDiagram'
    APARTMENTLIGHTSWITCH = 'ApartmentLightSwitch'
    APARTMENTMIRROR = 'ApartmentMirror'
    CAPECHOOSER = 'CapeChooser'
    COMPANIONSHELLCHOOSER = 'CompanionShellChooser'
    SWORDCHOOSER = 'SwordChooser'
    STAMINARECHARGER = 'StaminaRecharger'
    CHAINDASHSCOREBOARD = 'ChainDashScoreBoard'
    CHAINDASHSCOREBOARDPRO = 'ChainDashScoreBoardPro'
    WELLTOWER = 'WellTower'
    WATERFLOOR = 'WaterFloor'
    SNOWFLOOR = 'SnowFloor'
    WATERFALLREGION = 'WaterFallRegion'
    TITANHEART = 'TitanHeart'
    TITANEYE = 'TitanEye'
    GOOCIRCLE = 'GooCircle'
    SOCCERBALL = 'SoccerBall'
    SOCCERSCOREBOARD = 'SoccerScoreBoard'
    ABYSSDOOR = 'AbyssDoor'
    ABYSSDOORPILLAR = 'AbyssDoorPillar'
    SNOWPILE = 'SnowPile'
    VINEBOTTOM = 'VineBottom'
    INTERACTIVEOBJ = 'InteractiveObj'
    SCENERYLIGHT = 'SceneryLight'
    DOORINTERACTIVESYSTEM = 'DoorInteractiveSystem'
    SWITCHPARENT = 'SwitchParent'
    FLOORBUTTON = 'FloorButton'
    SWITCHPILLAR = 'SwitchPillar'
    TIMEDSWITCHPILLAR = 'TimedSwitchPillar'
    SLOWSWITCH = 'SlowSwitch'
    SPLITTINGDOOR = 'SplittingDoor'
    SINKINGDOOR = 'SinkingDoor'
    TOWER = 'Tower'
    DANGER = 'Danger'
    ACIDPARENT = 'AcidParent'
    LASERHAZARD = 'LaserHazard'
    ACIDPOOL = 'AcidPool'
    ACIDPOOLSHRINK = 'AcidPoolShrink'
    POPUPTURRET = 'PopUpTurret'
    CRUSHBLOCK = 'CrushBlock'
    MOVINGPLATFORM = 'MovingPlatform'
    RISINGPLATFORM = 'RisingPlatform'
    DROPPLATFORM = 'DropPlatform'
    SICKAREA = 'SickArea'
    PHASEMINE = 'PhaseMine'
    FLAMEPOLE = 'FlamePole'
    FLAMEVENT = 'FlameVent'
    FLAMETHROWER = 'FlameThrower'
    LINKMINE = 'linkMine'
    SINKINGPLATFORM = 'SinkingPlatform'
    SHALLOWPLATFORM = 'ShallowPlatform'
    WARPBLOCKTRAP = 'WarpBlockTrap'
    TIMEPOLE = 'TimePole'
    TURRET = 'Turret'
    TIMESLOWER = 'TimeSlower'
    FLAMEJET = 'FlameJet'
    TURRETLASER = 'TurretLaser'
    TURRETORB = 'TurretOrb'
    PHASEDROPPLATFORM = 'PhaseDropPlatform'
    MINE = 'Mine'
    OTTERBODY = 'OtterBody'
    ACIDLAKE = 'AcidLake'
    PHASEPLATFORM = 'PhasePlatform'
    DESTRUCTOR = 'Destructor'
    ENEMYSHOUT = 'EnemyShout'
    OTHERCOMPANION = 'OtherCompanion'
    ENEMYBOMB = 'EnemyBomb'
    GOALBOMB = 'GoalBomb'
    CULTCHARGE = 'CultCharge'
    ENEMYWEAPONCOL = 'enemyWeaponCol'
    CRYSTALSPIKE = 'CrystalSpike'
    TIMEPHASEBULLET = 'TimePhaseBullet'
    NINJASTAR = 'NinjaStar'
    LASERSHOT = 'LaserShot'
    ENEMYSHOT = 'enemyshot'
    ROCKET = 'rocket'
    ENEMYBULLET = 'EnemyBullet'
    MAGICMISSILE = 'magicmissile'
    HALDRIFTER = 'HALDrifter'
    DEADHALLUCINATION = 'deadHallucination'
    HALDIRK = 'HALdirk'
    ENEMYPLOPPER = 'EnemyPlopper'
    TESTENEMY = 'TestEnemy'
    PARRYPRINCE = 'ParryPrince'
    TANUKISPEAR = 'TanukiSpear'
    CRYSTALSPIDER = 'CrystalSpider'
    ALPHAWOLF = 'AlphaWolf'
    NINJAFROG = 'NinjaFrog'
    JARFROG = 'JarFrog'
    STRIDER = 'Strider'
    SWOOPNSPIT = 'SwoopNSpit'
    GARBAGEPLANT = 'GarbagePlant'
    DROPBIRD = 'DropBird'
    DIVEBOMB = 'DiveBomb'
    CRAB = 'Crab'
    CRABMAN = 'CrabMan'
    BURSTBIRD = 'BurstBird'
    SUMMONBLOCKBIRD = 'SummonBlockBird'
    DIRK = 'dirk'
    RIFLEDIRK = 'RifleDirk'
    MISSILEDIRK = 'missiledirk'
    SLIME = 'slime'
    LEAPER = 'Leaper'
    SPIDER = 'spider'
    DIRKOMMANDER = 'Dirkommander'
    PUNCHINGBAG = 'PunchingBag'
    WEAKPUNCHINGBAG = 'WeakPunchingBag'
    REGPUNCHINGBAG = 'RegPunchingBag'
    TANUKISWORD = 'TanukiSword'
    TANUKIGUN = 'TanukiGun'
    SMALLCRYSTALSPIDER = 'SmallCrystalSpider'
    CRYSTALBABY = 'CrystalBaby'
    WOLF = 'Wolf'
    NINJASTARFROG = 'NinjaStarFrog'
    SPIRALBOMBFROG = 'SpiralBombFrog'
    GRUMPSHROOM = 'Grumpshroom'
    MELTY = 'Melty'
    GHOSTBEAMBIRD = 'GhostBeamBird'
    CULTBIRD = 'CultBird'
    BIRDMAN = 'Birdman'
    SOUTHDRONE = 'SouthDrone'
    ROBODOG = 'RoboDog'
    BLADIRK = 'BlaDirk'
    HALBOSS = 'HalBoss'
    CLEANER = 'Cleaner'
    OLDGENERAL = 'OldGeneral'
    JERKPOPE = 'JerkPope'
    MARKSCYTHE = 'MarkScythe'
    BENNYARROW = 'BennyArrow'
    BULLETBAKER = 'BulletBaker'
    ALUCARDMODULESOCKET = 'AlucardModuleSocket'
    COUNTALUCARD = 'CountAlucard'
    TANUKICRYSTAL = 'TanukiCrystal'
    GEARBITSPAWNER = 'GearBitSpawner'
    HALEXPLOSION = 'HalExplosion'
    HALARM = 'HalArm'
    DIAMONDEYE = 'DiamondEye'
    EMBERDIAMOND = 'EmberDiamond'
    EMBERARM = 'EmberArm'
    EMBERARMPIECE = 'EmberArmPiece'
    EMBERLASER = 'EmberLaser'
    GUNSLINGER = 'GunSlinger'
    CRYSTALQUEEN = 'CrystalQueen'
    SPIDEREGG = 'SpiderEgg'
    ALUCARDDRONE = 'AlucardDrone'
    ARROWSTRIKE = 'ArrowStrike'
    SCYTHE = 'Scythe'
    WARPTRAVELER = 'WarpTraveler'
    DIAMONDSPIDER = 'DiamondSpider'
    CRYSTALSPIKEMAKER = 'CrystalSpikeMaker'
    CRYSTALWALLMAKER = 'CrystalWallMaker'
    DIAMONDSPIDERLEG = 'DiamondSpiderLeg'
    BOSSGEARBITSPAWNER = 'BossGearbitSpawner'
    BLOODPICKUP = 'BloodPickup'
    COMPANIONSUIT = 'CompanionSuit'
    BETACAPEPICKUP = 'BetaCapePickup'
    POWERUP = 'Powerup'
    POWDRONE = 'PowDrone'
    POWBUBBLEDRONE = 'PowBubbleDrone'
    POWSTUNDRONE = 'PowStunDrone'
    WAYPOINT = 'WayPoint'
    LIZARDFAMILY = 'LizardFamily'
    CHANTBIRD = 'ChantBird'
    NPCGENERIC = 'NPCGeneric'
    NPCALTDRIFTER = 'NPCAltDrifter'
    NPC = 'npc'
    CITIZEN = 'Citizen'
    BUFFALO = 'Buffalo'
    BADASSDRIFTER = 'BadassDrifter'
    BADASSINAPARTMENT = 'BadassInApartment'
    BADASSINOFFICE = 'BadassInOffice'
    NPCCUSTOMBASE = 'NPCCustomBase'
    DIRKGOALIE = 'DirkGoalie'
    EMBERFOX = 'EmberFox'
    ABYSSDOG = 'AbyssDog'
    JARFROGCARRY = 'JarFrogCarry'
    FROGDRAGOTTER = 'FrogDragOtter'
    TADPOLE = 'Tadpole'
    FLY = 'Fly'
    TINYFLY = 'TinyFly'
    EEL = 'Eel'
    SNAIL = 'Snail'
    BIRDMANFLYAWAY = 'BirdManFlyaway'
    FISH = 'fish'
    DOG = 'Dog'
    SQUIRREL = 'Squirrel'
    DEER = 'Deer'
    ROBIN = 'Robin'
    CROW = 'Crow'
    HALBIRD = 'HalBird'
    HERON = 'Heron'
    WILDDRONE = 'WildDrone'
    SQUIDBOT = 'SquidBot'
    SCORPBOT = 'ScorpBot'
    BIRD = 'bird'
    BIRDBLACK = 'BirdBlack'
    WILDLIFE = 'WildLife'
    WEATHEROBJ = 'weatherobj'
    BLACKRAIN = 'BlackRain'
    COLORREGION = 'ColorRegion'
    SCREENDUST = 'ScreenDust'
    TINYDUST = 'TinyDust'
    RAINBOWGLITTER = 'RainbowGlitter'
    PULSER = 'Pulser'
    WATERSPARKLE = 'WaterSparkle'
    RAINBOWBGDUST = 'RainbowBGDust'
    SNOWMAKER = 'SnowMaker'
    SLOWSNOW = 'SlowSnow'
    RAINMAKER = 'rainmaker'
    LEAKYRAIN = 'LeakyRain'
    LEAKYRAINPART = 'LeakyRainPart'
    BLACKRAINMAKER = 'BlackRainMaker'
    CLOUDS = 'Clouds'
    FGMIST = 'FGMist'
    LIGHTNING = 'Lightning'
    CLOUDWRAP = 'CloudWrap'
    RAIN = 'rain'
    SNOW = 'snow'
    DUSTPART = 'dustpart'
    DASHBLOCK = 'DashBlock'
    BLOCK = 'block'
    SOFTBLOCK = 'SoftBlock'
    BLOCK2 = 'block2'
    BLOCKPATHFINDLESS = 'blockPathfindless'
    PARTBLOCK = 'PartBlock'
    OVERWALL = 'OverWall'
    UNDERWALL = 'UnderWall'
    SAFEPLATFORM = 'SafePlatform'
    PROTECTIONPLATFORM = 'ProtectionPlatform'
    SECONDARY = 'Secondary'
    ROOMMAPDATA = 'RoomMapData'
    DRAWPOINT = 'DrawPoint'
    DRAWLINE = 'DrawLine'
    DRAWCIRCLE = 'DrawCircle'
    DRAWOVAL = 'DrawOval'
    DRAWTEXT = 'DrawText'
    ATTACKCOL = 'attackcol'
    HITCOLLIDER = 'HitCollider'
    CHAR = 'char'
    DECOY = 'Decoy'
    PHANTOMSLASH = 'PhantomSlash'
    CHARHITMASK = 'charHitMask'
    DEADCHAR = 'deadchar'
    DEADP2 = 'deadP2'
    GHOST = 'ghost'
    ALTCOMPANION = 'AltCompanion'
    ORB = 'Orb'
    ROLLYPOLLY = 'rollyPolly'
    ROLLYROCKET = 'rollyRocket'
    CRYSTALLANCE = 'CrystalLance'
    CRYSTALMARKER = 'CrystalMarker'
    CRYSTALMAKER = 'CrystalMaker'
    CRYSTAL = 'Crystal'
    DIAMONDBULLET = 'diamondBullet'
    BYUUBLOCKCOLLIDER = 'ByuuBlockCollider'
    BOMB = 'bomb'
    LEAPFLAME = 'LeapFlame'
    RAILLASER = 'RailLaser'
    CANNONCHUNK = 'CannonChunk'
    WARPHAMMER = 'WarpHammer'
    HOLOAIMER = 'HoloAimer'
    CHARFIRESHADOW = 'CharFireShadow'
    BLASTSHOCKWAVE = 'BlastShockwave'
    BLAST = 'blast'
    BOUNCESPARK = 'BounceSpark'
    DROPLET = 'droplet'
    DUSTPILLAR = 'dustPillar'
    FADEDEBRI = 'FadeDebri'
    BREAKDEBRI = 'BreakDebri'
    SPINDEBRI = 'SpinDebri'
    FIRE = 'fire'
    FLAG = 'Flag'
    FOOTPRINT = 'footPrint'
    GRASSCLIPPING = 'grassclipping'
    IMAGEFADE = 'imageFade'
    IMAGESTAY = 'imagestay'
    IMAGEPART = 'imagePart'
    MEATBLAST = 'MeatBlast'
    SHATTER = 'shatter'
    SNAPFX = 'SnapFX'
    SPARKFLASH = 'sparkflash'
    SPARKSHOWER = 'sparkshower'
    SPLASH = 'splash'
    TELEPORTERFX = 'teleporterfx'
    BLOODPART = 'bloodpart'
    BLOODSPRAY = 'bloodspray'
    BLOODSTAIN = 'BloodStain'
    VIRUSSTAIN = 'VirusStain'
    GIBLET = 'giblet'
    FRIEDGIB = 'friedgib'
    TELEPORTFX = 'teleportfx'
    GOGGLETRAIL = 'goggletrail'
    DASHDIAMOND = 'DashDiamond'
    BURNTGROUND = 'BurntGround'
    DEATHDUST = 'deathdust'
    SMOKESMALL = 'smokesmall'
    SMOKE = 'smoke'
    ROCKETSPLIT = 'rocketsplit'
    EXPLOSIONPARTICLE = 'explosionParticle'
    DUSTDASH = 'dustdash'
    MISSILESMOKE = 'missilesmoke'
    PARRYFLASH = 'parryflash'
    RUNDUST = 'rundust'
    SHIELDDUST = 'shielddust'
    IMPACTDUST = 'ImpactDust'
    SMOKESPAWN = 'SmokeSpawn'
    DUSTBALL = 'DustBall'
    SLIMETRAIL = 'slimeTrail'
    SLIMEPART = 'slimePart'
    TWOFRAMEDEATH = 'TwoFrameDeath'
    BIRDMANTUMBLE = 'BirdmanTumble'
    MUZZLEFLASH = 'muzzleflash'
    ZELISKAEMMITTER = 'ZeliskaEmmitter'
    RAILLASERFADE = 'RailLaserFade'
    SHIELDPUSHSMALL = 'ShieldPushSmall'
    SHIELDPUSHMEDIUM = 'ShieldPushMedium'
    SHIELDPUSHLARGE = 'ShieldPushLarge'
    MASTERMUFFLER = 'masterMuffler'
    XPSOUND = 'xpSound'
    MISSILEHALF = 'MissileHalf'
    FIREONGROUND = 'FireOnGround'
    EXECUTEDELAYEDOBJ = 'ExecuteDelayedObj'
    OBJCTTVIDEOPLAYER = 'objCttVideoPlayer'
    WELLTERMINAL = 'WellTerminal'
    WELLPILLAR = 'WellPillar'
    PHASECRYSTAL = 'PhaseCrystal'
    WKEYPHASEBLOCK = 'WKeyPhaseBlock'
    WESTKEY = 'WestKey'
    CUTSHRUB = 'CutShrub'
    ABYREGIONWALL = 'AbyRegionWall'

#ifndef __AS__TYPE_
#define __AS__TYPE_
typedef struct {
	unsigned char bit0  : 1;
	unsigned char bit1  : 1;
	unsigned char bit2  : 1;
	unsigned char bit3  : 1;
	unsigned char bit4  : 1;
	unsigned char bit5  : 1;
	unsigned char bit6  : 1;
	unsigned char bit7  : 1;
} _1byte_bit_field_;

typedef struct {
	unsigned short bit0  : 1;
	unsigned short bit1  : 1;
	unsigned short bit2  : 1;
	unsigned short bit3  : 1;
	unsigned short bit4  : 1;
	unsigned short bit5  : 1;
	unsigned short bit6  : 1;
	unsigned short bit7  : 1;
	unsigned short bit8  : 1;
	unsigned short bit9  : 1;
	unsigned short bit10 : 1;
	unsigned short bit11 : 1;
	unsigned short bit12 : 1;
	unsigned short bit13 : 1;
	unsigned short bit14 : 1;
	unsigned short bit15 : 1;
} _2byte_bit_field_;

typedef struct {
	unsigned long bit0  : 1;
	unsigned long bit1  : 1;
	unsigned long bit2  : 1;
	unsigned long bit3  : 1;
	unsigned long bit4  : 1;
	unsigned long bit5  : 1;
	unsigned long bit6  : 1;
	unsigned long bit7  : 1;
	unsigned long bit8  : 1;
	unsigned long bit9  : 1;
	unsigned long bit10 : 1;
	unsigned long bit11 : 1;
	unsigned long bit12 : 1;
	unsigned long bit13 : 1;
	unsigned long bit14 : 1;
	unsigned long bit15 : 1;
	unsigned long bit16 : 1;
	unsigned long bit17 : 1;
	unsigned long bit18 : 1;
	unsigned long bit19 : 1;
	unsigned long bit20 : 1;
	unsigned long bit21 : 1;
	unsigned long bit22 : 1;
	unsigned long bit23 : 1;
	unsigned long bit24 : 1;
	unsigned long bit25 : 1;
	unsigned long bit26 : 1;
	unsigned long bit27 : 1;
	unsigned long bit28 : 1;
	unsigned long bit29 : 1;
	unsigned long bit30 : 1;
	unsigned long bit31 : 1;
} _4byte_bit_field_;
#endif

#ifndef __AS__TYPE_Alarm
#define __AS__TYPE_Alarm
typedef struct Alarm
{	plcbit Status;
	plcwstring Description[81];
	unsigned char Severity;
	plcbit Acknowledgement;
} Alarm;
#endif

#ifndef __AS__TYPE_McAxisPLCopenStateEnum
#define __AS__TYPE_McAxisPLCopenStateEnum
typedef enum McAxisPLCopenStateEnum
{	mcAXIS_DISABLED = 0,
	mcAXIS_STANDSTILL = 1,
	mcAXIS_HOMING = 2,
	mcAXIS_STOPPING = 3,
	mcAXIS_DISCRETE_MOTION = 4,
	mcAXIS_CONTINUOUS_MOTION = 5,
	mcAXIS_SYNCHRONIZED_MOTION = 6,
	mcAXIS_ERRORSTOP = 7,
	mcAXIS_STARTUP = 8,
	mcAXIS_INVALID_CONFIGURATION = 9,
} McAxisPLCopenStateEnum;
#endif

#ifndef __AS__TYPE_McHomingModeEnum
#define __AS__TYPE_McHomingModeEnum
typedef enum McHomingModeEnum
{	mcHOMING_DIRECT = 0,
	mcHOMING_SWITCH_GATE = 1,
	mcHOMING_ABSOLUTE_SWITCH = 2,
	mcHOMING_LIMIT_SWITCH = 4,
	mcHOMING_ABSOLUTE = 5,
	mcHOMING_DCM = 7,
	mcHOMING_BLOCK_TORQUE = 9,
	mcHOMING_BLOCK_LAG_ERROR = 10,
	mcHOMING_ABSOLUTE_INTERNAL = 11,
	mcHOMING_ABSOLUTE_CORRECTION = 133,
	mcHOMING_DCM_CORRECTION = 135,
	mcHOMING_DEFAULT = 140,
	mcHOMING_INIT = 141,
	mcHOMING_RESTORE_POSITION = 142,
} McHomingModeEnum;
#endif

#ifndef __AS__TYPE_McSwitchEnum
#define __AS__TYPE_McSwitchEnum
typedef enum McSwitchEnum
{	mcSWITCH_OFF = 0,
	mcSWITCH_ON = 1,
} McSwitchEnum;
#endif

#ifndef __AS__TYPE_McCommunicationStateEnum
#define __AS__TYPE_McCommunicationStateEnum
typedef enum McCommunicationStateEnum
{	mcCOMM_STATE_NOT_ACTIVE = 0,
	mcCOMM_STATE_WAITING = 100,
	mcCOMM_STATE_CONNECTED = 200,
	mcCOMM_STATE_FW_UPDATE = 300,
	mcCOMM_STATE_CONFIG = 400,
	mcCOMM_STATE_ACTIVATING = 500,
	mcCOMM_STATE_ACTIVE = 600,
	mcCOMM_STATE_INACTIVE = 700,
	mcCOMM_STATE_FAILED = 1000,
} McCommunicationStateEnum;
#endif

#ifndef __AS__TYPE_McInternalMappLinkType
#define __AS__TYPE_McInternalMappLinkType
typedef struct McInternalMappLinkType
{	unsigned long Internal[2];
} McInternalMappLinkType;
#endif

#ifndef __AS__TYPE_McInternalAxisIfType
#define __AS__TYPE_McInternalAxisIfType
typedef struct McInternalAxisIfType
{	plcdword vtable;
} McInternalAxisIfType;
#endif

#ifndef __AS__TYPE_McAxisType
#define __AS__TYPE_McAxisType
typedef struct McAxisType
{	struct McInternalAxisIfType(* controlif);
	McInternalMappLinkType mappLinkInternal;
	signed long seqNo;
} McAxisType;
#endif

#ifndef __AS__TYPE_MpComFacilitiesEnum
#define __AS__TYPE_MpComFacilitiesEnum
typedef enum MpComFacilitiesEnum
{	mpCOM_FAC_UNDEFINED = -1,
	mpCOM_FAC_ARCORE = 0,
	mpCOM_FAC_SAFETY1 = 1,
	mpCOM_FAC_SAFETY2 = 2,
	mpCOM_FAC_GMC1 = 96,
	mpCOM_FAC_GMC2 = 97,
	mpCOM_FAC_GMCAXIS = 98,
	mpCOM_FAC_GMCAXESGROUP = 99,
	mpCOM_FAC_GMCARNCGROUP = 103,
	mpCOM_FAC_TRF = 105,
	mpCOM_FAC_MAPP_INTERNAL = 144,
	mpCOM_FAC_MAPP_CORE = 145,
	mpCOM_FAC_MAPP_INFRASTRUCTURE = 146,
	mpCOM_FAC_MAPP_MECHATRONIC = 147,
	mpCOM_FAC_MAPP_INDUSTRY = 148,
} MpComFacilitiesEnum;
#endif

#ifndef __AS__TYPE_MpComSeveritiesEnum
#define __AS__TYPE_MpComSeveritiesEnum
typedef enum MpComSeveritiesEnum
{	mpCOM_SEV_SUCCESS = 0,
	mpCOM_SEV_INFORMATIONAL = 1,
	mpCOM_SEV_WARNING = 2,
	mpCOM_SEV_ERROR = 3,
} MpComSeveritiesEnum;
#endif

#ifndef __AS__TYPE_MpComInternalDataType
#define __AS__TYPE_MpComInternalDataType
typedef struct MpComInternalDataType
{	unsigned long pObject;
	unsigned long State;
} MpComInternalDataType;
#endif

#ifndef __AS__TYPE_McDirectionEnum
#define __AS__TYPE_McDirectionEnum
typedef enum McDirectionEnum
{	mcDIR_POSITIVE = 0,
	mcDIR_NEGATIVE = 1,
	mcDIR_CURRENT = 2,
	mcDIR_SHORTEST_WAY = 3,
	mcDIR_EXCEED_PERIOD = 8,
	mcDIR_UNDEFINED = 9,
	mcDIR_BOTH = 10,
} McDirectionEnum;
#endif

#ifndef __AS__TYPE_MpAxisHomingOptionsType
#define __AS__TYPE_MpAxisHomingOptionsType
typedef struct MpAxisHomingOptionsType
{	float StartVelocity;
	float HomingVelocity;
	float Acceleration;
	McDirectionEnum SwitchEdge;
	McDirectionEnum StartDirection;
	McDirectionEnum HomingDirection;
	McSwitchEnum ReferencePulse;
	McSwitchEnum KeepDirection;
	float ReferencePulseBlockingDistance;
	float TorqueLimit;
	float BlockDetectionPositionError;
	float PositionErrorStopLimit;
	unsigned long RestorePositionVariableAddress;
	McSwitchEnum DriveSpecificHoming;
	signed char DriveSpecificHomingMode;
	double SensorOffset;
	McDirectionEnum SensorOffsetDirection;
	McSwitchEnum DisableRestorePositionOnEnable;
} MpAxisHomingOptionsType;
#endif

#ifndef __AS__TYPE_MpAxisHomingType
#define __AS__TYPE_MpAxisHomingType
typedef struct MpAxisHomingType
{	McHomingModeEnum Mode;
	double Position;
	MpAxisHomingOptionsType Options;
} MpAxisHomingType;
#endif

#ifndef __AS__TYPE_MpAxisJogLimitPositionType
#define __AS__TYPE_MpAxisJogLimitPositionType
typedef struct MpAxisJogLimitPositionType
{	double FirstPosition;
	double LastPosition;
} MpAxisJogLimitPositionType;
#endif

#ifndef __AS__TYPE_MpAxisJogType
#define __AS__TYPE_MpAxisJogType
typedef struct MpAxisJogType
{	float Velocity;
	float Acceleration;
	float Deceleration;
	MpAxisJogLimitPositionType LimitPosition;
	float Jerk;
} MpAxisJogType;
#endif

#ifndef __AS__TYPE_MpAxisStopAtPositionType
#define __AS__TYPE_MpAxisStopAtPositionType
typedef struct MpAxisStopAtPositionType
{	plcbit Activate;
	float Deceleration;
	double Position;
} MpAxisStopAtPositionType;
#endif

#ifndef __AS__TYPE_MpAxisStopType
#define __AS__TYPE_MpAxisStopType
typedef struct MpAxisStopType
{	float Deceleration;
	float Jerk;
	MpAxisStopAtPositionType StopAtPosition;
} MpAxisStopType;
#endif

#ifndef __AS__TYPE_MpAxisLimitLoadType
#define __AS__TYPE_MpAxisLimitLoadType
typedef struct MpAxisLimitLoadType
{	float Load;
	McDirectionEnum Direction;
} MpAxisLimitLoadType;
#endif

#ifndef __AS__TYPE_MpAxisAutoTuneModeEnum
#define __AS__TYPE_MpAxisAutoTuneModeEnum
typedef enum MpAxisAutoTuneModeEnum
{	mcAXIS_TUNE_AUTOMATIC = 0,
	mcAXIS_TUNE_SPEED = 1,
	mcAXIS_TUNE_POSITION = 2,
	mcAXIS_TUNE_TEST = 3,
	mcAXIS_TUNE_LOOP_FILTER = 4,
	mcAXIS_TUNE_FEED_FORWARD = 5,
} MpAxisAutoTuneModeEnum;
#endif

#ifndef __AS__TYPE_McAcpAxAutoTuneOrientationEnum
#define __AS__TYPE_McAcpAxAutoTuneOrientationEnum
typedef enum McAcpAxAutoTuneOrientationEnum
{	mcACPAX_ORIENTATION_HORIZONTAL = 0,
	mcACPAX_ORIENTATION_VERTICAL = 1,
} McAcpAxAutoTuneOrientationEnum;
#endif

#ifndef __AS__TYPE_MpAxisAutoTuneLoopFilterModeEnum
#define __AS__TYPE_MpAxisAutoTuneLoopFilterModeEnum
typedef enum MpAxisAutoTuneLoopFilterModeEnum
{	mcAXIS_TUNE_LOOP_FILTER_F1 = 0,
	mcAXIS_TUNE_LOOP_FILTER_F1_F2 = 1,
	mcAXIS_TUNE_LOOP_FILTER_F1_F2_F3 = 2,
} MpAxisAutoTuneLoopFilterModeEnum;
#endif

#ifndef __AS__TYPE_McAcpAxLoopFilterModeEnum
#define __AS__TYPE_McAcpAxLoopFilterModeEnum
typedef enum McAcpAxLoopFilterModeEnum
{	mcACPAX_LOOP_FILTER_IGNORE = 0,
	mcACPAX_LOOP_FILTER_USE = 1,
	mcACPAX_LOOP_FILTER_TUNE_NOTCH = 2,
} McAcpAxLoopFilterModeEnum;
#endif

#ifndef __AS__TYPE_McAcpAxFilterTimeModeEnum
#define __AS__TYPE_McAcpAxFilterTimeModeEnum
typedef enum McAcpAxFilterTimeModeEnum
{	mcACPAX_FILTER_TIME_USE = 0,
	mcACPAX_FILTER_TIME_TUNE_MODE1 = 1,
	mcACPAX_FILTER_TIME_TUNE_MODE2 = 2,
} McAcpAxFilterTimeModeEnum;
#endif

#ifndef __AS__TYPE_MpAxisAutoTuneOptionsType
#define __AS__TYPE_MpAxisAutoTuneOptionsType
typedef struct MpAxisAutoTuneOptionsType
{	float MaxProportionalGain;
	McAcpAxLoopFilterModeEnum SpeedTuneLoopFilter1Mode;
	McAcpAxFilterTimeModeEnum SpeedTuneFilterTmeMode;
} MpAxisAutoTuneOptionsType;
#endif

#ifndef __AS__TYPE_McAcpAxAutoTuneFeedFwdModeEnum
#define __AS__TYPE_McAcpAxAutoTuneFeedFwdModeEnum
typedef enum McAcpAxAutoTuneFeedFwdModeEnum
{	mcACPAX_TUNE_FF_MODE_STANDARD = 0,
	mcACPAX_TUNE_FF_MODE_PASSIVE = 1,
} McAcpAxAutoTuneFeedFwdModeEnum;
#endif

#ifndef __AS__TYPE_MpAxisAutoTuneFFOptionsType
#define __AS__TYPE_MpAxisAutoTuneFFOptionsType
typedef struct MpAxisAutoTuneFFOptionsType
{	McAcpAxAutoTuneFeedFwdModeEnum Mode;
	McDirectionEnum Direction;
	float MaxVelocityPercent;
	float Acceleration;
} MpAxisAutoTuneFFOptionsType;
#endif

#ifndef __AS__TYPE_MpAxisAutoTuneType
#define __AS__TYPE_MpAxisAutoTuneType
typedef struct MpAxisAutoTuneType
{	MpAxisAutoTuneModeEnum Mode;
	McAcpAxAutoTuneOrientationEnum Orientation;
	float MaxCurrentPercent;
	double MaxDistance;
	double MaxPositionError;
	plcbit SaveControllerSettings;
	MpAxisAutoTuneLoopFilterModeEnum LoopFilterMode;
	MpAxisAutoTuneOptionsType Options;
	MpAxisAutoTuneFFOptionsType FeedForward;
} MpAxisAutoTuneType;
#endif

#ifndef __AS__TYPE_MpAxisBasicParType
#define __AS__TYPE_MpAxisBasicParType
typedef struct MpAxisBasicParType
{	double Position;
	double Distance;
	float Velocity;
	float Acceleration;
	float Deceleration;
	McDirectionEnum Direction;
	MpAxisHomingType Homing;
	MpAxisJogType Jog;
	MpAxisStopType Stop;
	MpAxisLimitLoadType LimitLoad;
	MpAxisAutoTuneType AutoTune;
	float Jerk;
} MpAxisBasicParType;
#endif

#ifndef __AS__TYPE_McDigitalInputStatusType
#define __AS__TYPE_McDigitalInputStatusType
typedef struct McDigitalInputStatusType
{	plcbit HomingSwitch;
	plcbit PositiveLimitSwitch;
	plcbit NegativeLimitSwitch;
	plcbit Trigger1;
	plcbit Trigger2;
	plcbit DriveEnable;
} McDigitalInputStatusType;
#endif

#ifndef __AS__TYPE_MpAxisErrorEnum
#define __AS__TYPE_MpAxisErrorEnum
typedef enum MpAxisErrorEnum
{	mcAXIS_NO_ERROR = 0,
	mcAXIS_ERR_PLC_OPEN = -1067278080,
	mcAXIS_WRN_PLC_OPEN = -2141019903,
	mcAXIS_WRN_MULTIPLE_COMMAND = -2141019902,
	mcAXIS_ERR_RECOVERY_NOT_ALLOWED = -1067278072,
	mcAXIS_WRN_RESTOREPOS_INVALID = -2141019895,
	mcAXIS_ERR_ACTIVATION = -1064239103,
	mcAXIS_ERR_MPLINK_NULL = -1064239102,
	mcAXIS_ERR_MPLINK_INVALID = -1064239101,
	mcAXIS_ERR_MPLINK_CHANGED = -1064239100,
	mcAXIS_ERR_MPLINK_CORRUPT = -1064239099,
	mcAXIS_ERR_MPLINK_IN_USE = -1064239098,
	mcAXIS_ERR_PAR_NULL = -1064239097,
} MpAxisErrorEnum;
#endif

#ifndef __AS__TYPE_MpAxisStatusIDType
#define __AS__TYPE_MpAxisStatusIDType
typedef struct MpAxisStatusIDType
{	MpAxisErrorEnum ID;
	MpComSeveritiesEnum Severity;
	unsigned short Code;
} MpAxisStatusIDType;
#endif

#ifndef __AS__TYPE_MpAxisInternalType
#define __AS__TYPE_MpAxisInternalType
typedef struct MpAxisInternalType
{	signed long ID;
	MpComSeveritiesEnum Severity;
	MpComFacilitiesEnum Facility;
	unsigned short Code;
} MpAxisInternalType;
#endif

#ifndef __AS__TYPE_MpAxisExecutingCmdEnum
#define __AS__TYPE_MpAxisExecutingCmdEnum
typedef enum MpAxisExecutingCmdEnum
{	mcAXIS_CMD_IDLE = 0,
	mcAXIS_CMD_HOMING = 1,
	mcAXIS_CMD_STOP = 2,
	mcAXIS_CMD_HALT = 3,
	mcAXIS_CMD_MOVE_VELOCITY = 4,
	mcAXIS_CMD_MOVE_ABSOLUTE = 5,
	mcAXIS_CMD_MOVE_ADDITIVE = 6,
	mcAXIS_CMD_JOG_POSITIVE = 7,
	mcAXIS_CMD_JOG_NEGATIVE = 8,
	mcAXIS_CMD_REMOTE_CONTROL = 9,
	mcAXIS_CMD_ERROR_RESET = 10,
	mcAXIS_CMD_GEAR = 11,
	mcAXIS_CMD_CAM = 12,
	mcAXIS_CMD_GEAR_IN_POS = 13,
	mcAXIS_CMD_OFFSET_SHIFT = 14,
	mcAXIS_CMD_PHASE_SHIFT = 15,
	mcAXIS_CMD_GET_CAM_POSITION = 16,
	mcAXIS_CMD_CAM_PREPARE = 17,
	mcAXIS_CMD_CAM_RECOVERY = 18,
	mcAXIS_CMD_CAM_SEQUENCE = 19,
	mcAXIS_CMD_PARLOCK = 20,
	mcAXIS_CMD_GET_SEQUENCE = 21,
	mcAXIS_CMD_SET_SEQUENCE = 22,
	mcAXIS_CMD_SIMULATION = 23,
	mcAXIS_CMD_STOP_AT_POSITION = 24,
	mcAXIS_CMD_POWER = 25,
	mcAXIS_CMD_AUTOTUNE = 26,
	mcAXIS_CMD_MOVE_CYCLIC_POSITION = 27,
	mcAXIS_CMD_MOVE_CYCLIC_VELOCITY = 28,
	mcAXIS_CMD_VELOCITY_CONTROL = 29,
	mcAXIS_CMD_TORQUE_CONTROL = 30,
	mcAXIS_CMD_TORQUE_FF = 31,
} MpAxisExecutingCmdEnum;
#endif

#ifndef __AS__TYPE_MpAxisDiagExtType
#define __AS__TYPE_MpAxisDiagExtType
typedef struct MpAxisDiagExtType
{	MpAxisStatusIDType StatusID;
	MpAxisInternalType Internal;
	MpAxisExecutingCmdEnum ExecutingCommand;
} MpAxisDiagExtType;
#endif

#ifndef __AS__TYPE_McLibraryInfoType
#define __AS__TYPE_McLibraryInfoType
typedef struct McLibraryInfoType
{	plcstring Name[33];
} McLibraryInfoType;
#endif

#ifndef __AS__TYPE_McAxisTypeEnum
#define __AS__TYPE_McAxisTypeEnum
typedef enum McAxisTypeEnum
{	mcAX_TYPE_ACP_REAL = 0,
	mcAX_TYPE_ACP_VIRT = 1,
	mcAX_TYPE_ACP_APSM = 2,
	mcAX_TYPE_ACP_PS_ACTIVE = 3,
	mcAX_TYPE_ACP_PS_PASSIVE = 4,
	mcAX_TYPE_ACP_EXT_ENC = 5,
	mcAX_TYPE_ACP_INV = 6,
	mcAX_TYPE_STP = 7,
	mcAX_TYPE_PURE_VIRT = 8,
	mcAX_TYPE_PURE_VIRT_GPAI = 9,
	mcAX_TYPE_DS402_SERVO = 10,
	mcAX_TYPE_DS402_INV = 11,
	mcAX_TYPE_PURE_VIRT_EXT_ENC = 12,
} McAxisTypeEnum;
#endif

#ifndef __AS__TYPE_McHwInfoAxisType
#define __AS__TYPE_McHwInfoAxisType
typedef struct McHwInfoAxisType
{	plcstring AxisName[33];
	plcstring ConfigElementLocation[251];
	McAxisTypeEnum AxisType;
} McHwInfoAxisType;
#endif

#ifndef __AS__TYPE_McHwInfoDriveType
#define __AS__TYPE_McHwInfoDriveType
typedef struct McHwInfoDriveType
{	plcstring ModelNumber[20];
	plcstring ModuleID[12];
	plcstring SerialNumber[20];
	plcstring Revision[12];
	plcstring FirmwareVersion[8];
} McHwInfoDriveType;
#endif

#ifndef __AS__TYPE_McHwInfoCardType
#define __AS__TYPE_McHwInfoCardType
typedef struct McHwInfoCardType
{	plcbit InfoAvailable;
	plcstring ModelNumber[20];
	plcstring SerialNumber[20];
	plcstring Revision[4];
} McHwInfoCardType;
#endif

#ifndef __AS__TYPE_McHwInfoMotorType
#define __AS__TYPE_McHwInfoMotorType
typedef struct McHwInfoMotorType
{	plcbit InfoAvailable;
	plcstring ModelNumber[36];
	plcstring SerialNumber[20];
	plcstring Revision[4];
} McHwInfoMotorType;
#endif

#ifndef __AS__TYPE_McHardwareInfoType
#define __AS__TYPE_McHardwareInfoType
typedef struct McHardwareInfoType
{	McHwInfoAxisType Axis;
	McHwInfoDriveType Drive;
	struct McHwInfoCardType Card[4];
	struct McHwInfoMotorType Motor[3];
} McHardwareInfoType;
#endif

#ifndef __AS__TYPE_McAutoTuneStateEnum
#define __AS__TYPE_McAutoTuneStateEnum
typedef enum McAutoTuneStateEnum
{	mcAT_NOT_ACTIVE = 0,
	mcAT_SPEED_CONTROLLER = 1,
	mcAT_POSTION_CONTROLLER = 2,
	mcAT_LOAD_MODEL = 3,
	mcAT_LOOP_FILTERS = 4,
	mcAT_FEED_FORWARD_STANDARD = 5,
	mcAT_FEED_FORWARD_PASSIVE = 6,
	mcAT_TEST = 7,
	mcAT_MOTOR_PHASING = 8,
	mcAT_INDUCTION_MOTOR = 9,
	mcAT_SYNCHRON_MOTOR = 10,
} McAutoTuneStateEnum;
#endif

#ifndef __AS__TYPE_McMechDevCompStateEnum
#define __AS__TYPE_McMechDevCompStateEnum
typedef enum McMechDevCompStateEnum
{	mcMDC_STATE_NOT_ACTIVE = 0,
	mcMDC_STATE_INIT = 1,
	mcMDC_STATE_ACTIVE_DIR_INDEP = 2,
	mcMDC_STATE_ACTIVE_DIR_DEP = 3,
	mcMDC_STATE_ERROR = 4,
} McMechDevCompStateEnum;
#endif

#ifndef __AS__TYPE_MpAxisBasicInfoType
#define __AS__TYPE_MpAxisBasicInfoType
typedef struct MpAxisBasicInfoType
{	plcbit CommunicationReady;
	plcbit ReadyToPowerOn;
	plcbit Simulation;
	plcbit Jogging;
	plcbit JogLimitReached;
	plcbit LimitLoadActive;
	McAxisPLCopenStateEnum PLCopenState;
	McDigitalInputStatusType DigitalInputsStatus;
	MpAxisDiagExtType Diag;
	McLibraryInfoType LibraryInfo;
	McCommunicationStateEnum CommunicationState;
	unsigned long StartupCount;
	plcbit AutoTuneDone;
	float AutoTuneQuality;
	McHardwareInfoType HardwareInfo;
	McAutoTuneStateEnum AutoTuneState;
	McMechDevCompStateEnum MechDeviationCompState;
} MpAxisBasicInfoType;
#endif

struct r_trig
{	plcbit CLK;
	plcbit Q;
	plcbit M;
};
_BUR_PUBLIC void r_trig(struct r_trig* inst);
struct f_trig
{	plcbit CLK;
	plcbit Q;
	plcbit M;
};
_BUR_PUBLIC void f_trig(struct f_trig* inst);
struct MpAxisBasic
{	struct McAxisType(* MpLink);
	struct MpAxisBasicParType(* Parameters);
	signed long StatusID;
	double Position;
	float Velocity;
	MpAxisBasicInfoType Info;
	MpComInternalDataType Internal;
	plcbit Enable;
	plcbit ErrorReset;
	plcbit Update;
	plcbit Power;
	plcbit Home;
	plcbit MoveVelocity;
	plcbit MoveAbsolute;
	plcbit MoveAdditive;
	plcbit Stop;
	plcbit JogPositive;
	plcbit JogNegative;
	plcbit LimitLoad;
	plcbit ReleaseBrake;
	plcbit Simulate;
	plcbit AutoTune;
	plcbit Active;
	plcbit Error;
	plcbit UpdateDone;
	plcbit CommandBusy;
	plcbit CommandAborted;
	plcbit PowerOn;
	plcbit IsHomed;
	plcbit InVelocity;
	plcbit InPosition;
	plcbit MoveActive;
	plcbit MoveDone;
	plcbit Stopped;
	plcbit LimitLoadReady;
	plcbit BrakeReleased;
};
_BUR_PUBLIC void MpAxisBasic(struct MpAxisBasic* inst);
_GLOBAL struct MpAxisBasic MpAxisBasic_0;
_GLOBAL MpAxisBasicParType AxisParam;
_GLOBAL Alarm Alarm1;
_GLOBAL McAxisType gAxis_1;
_LOCAL struct f_trig zzFTR000010000;
_LOCAL plcbit zzBOOL00010000;
_LOCAL plcbit zzBOOL00010001;
_LOCAL struct r_trig zzRTR000010000;

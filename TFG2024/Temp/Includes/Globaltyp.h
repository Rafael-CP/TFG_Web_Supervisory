/* Automation Studio generated header file */
/* Do not edit ! */

#ifndef _BUR_1722466073_1_
#define _BUR_1722466073_1_

#include <bur/plctypes.h>

/* Datatypes and datatypes of function blocks */
typedef struct Alarm
{	plcbit Status;
	plcwstring Description[81];
	unsigned char Severity;
	plcbit Acknowledgement;
} Alarm;






__asm__(".section \".plc\"");

/* Used IEC files */
__asm__(".ascii \"iecfile \\\"Logical/Global.typ\\\" scope \\\"global\\\"\\n\"");

/* Exported library functions and function blocks */

__asm__(".previous");


#endif /* _BUR_1722466073_1_ */


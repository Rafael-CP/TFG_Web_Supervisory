#define _DEFAULT_INCLUDE
#include <bur\plctypes.h>
#include "C:/Users/Rafael/Documents/UNIFEI/2024.1/TFG/TFG2024/Temp/Objects/Config1/X20CP0483/Axis1Ctrl/Initld.h"
#line 1 "C:/Users/Rafael/Documents/UNIFEI/2024.1/TFG/TFG2024/Logical/Axis1Ctrl/Init.nodebug"
#line 1 "C:/Users/Rafael/Documents/UNIFEI/2024.1/TFG/TFG2024/Logical/Axis1Ctrl/Init.ld"
void __BUR__ENTRY_INIT_FUNCT__(void){int __AS__Local0_00000;plcwstring* __AS__Local5_00000;plcwstring* __AS__Local6_00000;{(Alarm1.Status=(zzBOOL80010000=0));




__AS__Local5_00000=(plcwstring*)zz006580010000; __AS__Local6_00000=(plcwstring*)"\x4D\x00\x6F\x00\x74\x00\x6F\x00\x72\x00\x20\x00\x65\x00\x6D\x00\x20\x00\x65\x00\x73\x00\x74\x00\x61\x00\x64\x00\x6F\x00\x20\x00\x64\x00\x65\x00\x20\x00\x65\x00\x72\x00\x72\x00\x6F\x00\x21\x00\x00"; for(__AS__Local0_00000=0; __AS__Local0_00000<24l && __AS__Local6_00000[__AS__Local0_00000]!=0; __AS__Local0_00000++) __AS__Local5_00000[__AS__Local0_00000] = __AS__Local6_00000[__AS__Local0_00000]; __AS__Local5_00000[__AS__Local0_00000] = 0;__AS__Local5_00000=(plcwstring*)Alarm1.Description; __AS__Local6_00000=(plcwstring*)zz006580010000; for(__AS__Local0_00000=0; __AS__Local0_00000<80l && __AS__Local6_00000[__AS__Local0_00000]!=0; __AS__Local0_00000++) __AS__Local5_00000[__AS__Local0_00000] = __AS__Local6_00000[__AS__Local0_00000]; __AS__Local5_00000[__AS__Local0_00000] = 0;




(Alarm1.Severity=(zz000580010000=1));




(Alarm1.Acknowledgement=(zzBOOL80010001=0));


}
}
#line 1 "C:/Users/Rafael/Documents/UNIFEI/2024.1/TFG/TFG2024/Logical/Axis1Ctrl/Init.nodebug"

void __AS__ImplInitInit_ld(void){__BUR__ENTRY_INIT_FUNCT__();}

__asm__(".section \".plc\"");
__asm__(".ascii \"iecfile \\\"Logical/Global.typ\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/operator/operator.typ\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/runtime/runtime.typ\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/astime/astime.typ\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/AsIecCon/AsIecCon.typ\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/McBase/McBase.typ\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/McBase/McBaseCfg.typ\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/MpBase/MpBase.typ\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/MpAxis/MpAxis.typ\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/MpAxis/MpAxisError.typ\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/McAxis/McAxis.typ\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/McAxis/McAxisCfg.typ\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/McAcpAx/McAcpAx.typ\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/McAcpAx/McAcpAxCfg.typ\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/operator/operator.fun\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/runtime/runtime.fun\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/astime/astime.fun\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/AsIecCon/AsIecCon.fun\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/McBase/McBase.fun\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/MpBase/MpBase.fun\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/MpAxis/MpAxis.fun\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/McAxis/McAxis.fun\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/McAcpAx/McAcpAx.fun\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Global.var\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Temp/Includes/AS_TempDecl/Config1/GlobalComponents/McElements.var\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/operator/operator.var\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/runtime/runtime.var\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/astime/astime.var\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/AsIecCon/AsIecCon.var\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/McBase/McBase.var\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/MpBase/MpBase.var\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/McAxis/McAxis.var\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Libraries/McAcpAx/McAcpAx.var\\\" scope \\\"global\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Axis1Ctrl/Types.typ\\\" scope \\\"local\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Logical/Axis1Ctrl/Variables.var\\\" scope \\\"local\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"C:/Users/Rafael/Documents/UNIFEI/2024.1/TFG/TFG2024/Temp/Objects/Config1/X20CP0483/Axis1Ctrl/Init.ld.var\\\" scope \\\"local\\\"\\n\"");
__asm__(".ascii \"plcreplace \\\"C:/Users/Rafael/Documents/UNIFEI/2024.1/TFG/TFG2024/Temp/Objects/Config1/X20CP0483/Axis1Ctrl/Init.ld.c\\\" \\\"C:/Users/Rafael/Documents/UNIFEI/2024.1/TFG/TFG2024/Logical/Axis1Ctrl/Init.ld\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Temp/Objects/Config1/X20CP0483/Axis1Ctrl/Init.ld.var\\\" scope \\\"local\\\"\\n\"");
__asm__(".previous");

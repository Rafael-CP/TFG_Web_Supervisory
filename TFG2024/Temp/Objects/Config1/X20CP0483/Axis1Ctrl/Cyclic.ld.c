#define _DEFAULT_INCLUDE
#include <bur\plctypes.h>
#include "C:/Users/Rafael/Documents/UNIFEI/2024.1/TFG/TFG2024/Temp/Objects/Config1/X20CP0483/Axis1Ctrl/Cyclicld.h"
#line 1 "C:/Users/Rafael/Documents/UNIFEI/2024.1/TFG/TFG2024/Logical/Axis1Ctrl/Cyclic.nodebug"
#line 1 "C:/Users/Rafael/Documents/UNIFEI/2024.1/TFG/TFG2024/Logical/Axis1Ctrl/Cyclic.ld"
void _CYCLIC __BUR__ENTRY_CYCLIC_FUNCT__(void){{if((zzBOOL00010000=1)){

}else{goto imp1_EN0000;
}((*(unsigned long*)&(MpAxisBasic_0.MpLink))=((unsigned long)(&gAxis_1)));




(MpAxisBasic_0.Enable=1);

((*(unsigned long*)&(MpAxisBasic_0.Parameters))=((unsigned long)(&AxisParam)));




MpAxisBasic(&MpAxisBasic_0);
;

imp1_EN0000:(zzRTR000010000.CLK=MpAxisBasic_0.MoveDone);

r_trig(&zzRTR000010000);
(zzFTR000010000.CLK=MpAxisBasic_0.PowerOn);

f_trig(&zzFTR000010000);
if((zzBOOL00010001=(zzRTR000010000.Q|zzFTR000010000.Q))){


(MpAxisBasic_0.MoveAbsolute=0);
}if(zzBOOL00010001){
(MpAxisBasic_0.MoveAdditive=0);

}(Alarm1.Status=MpAxisBasic_0.Error);
}
}
#line 1 "C:/Users/Rafael/Documents/UNIFEI/2024.1/TFG/TFG2024/Logical/Axis1Ctrl/Cyclic.nodebug"

void __AS__ImplInitCyclic_ld(void){}

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
__asm__(".ascii \"iecfile \\\"C:/Users/Rafael/Documents/UNIFEI/2024.1/TFG/TFG2024/Temp/Objects/Config1/X20CP0483/Axis1Ctrl/Cyclic.ld.var\\\" scope \\\"local\\\"\\n\"");
__asm__(".ascii \"plcreplace \\\"C:/Users/Rafael/Documents/UNIFEI/2024.1/TFG/TFG2024/Temp/Objects/Config1/X20CP0483/Axis1Ctrl/Cyclic.ld.c\\\" \\\"C:/Users/Rafael/Documents/UNIFEI/2024.1/TFG/TFG2024/Logical/Axis1Ctrl/Cyclic.ld\\\"\\n\"");
__asm__(".ascii \"iecfile \\\"Temp/Objects/Config1/X20CP0483/Axis1Ctrl/Cyclic.ld.var\\\" scope \\\"local\\\"\\n\"");
__asm__(".previous");

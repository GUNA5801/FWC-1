.include "/sdcard/Download/FWC/assembly//m328Pdef.inc"
; Initialize registers
LDI R16, 0x00   ; Load 00 into R16
LDI R17, 0x00   ; Load 00 into R17
LDI R18, 0x03   ; Load 3 into R18 for comparison later
LDI R19, 0x01   ; Load 1 into R19 for toggling

LOOP:
    ; Wait for falling edge on clock
    SBIC PIND, 0    ; Skip next instruction if PD0 is low
    RJMP LOOP       ; Jump back to LOOP if clock is high

    ; Update D1 and D2 flip-flops
    AND R24, R17    ; (!Q1)*(!Q2) = Q1 & Q2
    LSL R24         ; Shift left one bit to prepare for D1
    OR R24, R16     ; Combine with current state for D1
    MOV R16, R17    ; Update D1_Q-1
    MOV R17, R24    ; Update D1_Q

    MOV R24, R16    ; Copy D1_Q to R24 for use in updating D2_Q
    ANDI R24, 0x01  ; Q1 = D1_Q & 0x01
    LSL R24         ; Shift left one bit to prepare for D2
    OR R24, R16     ; Combine with current state for D2
    MOV R16, R17    ; Update D2_Q-1
    MOV R17, R24    ; Update D2_Q

    ; Output D2 state
    OUT PORTB, R17  ; Output D2_Q

    ; Check for initial state of 00 and stop the loop
    CP R16, R18     ; Compare R16 (D1_Q-1) with 0x03
    BREQ END_LOOP   ; Branch to END_LOOP if equal

    ; Wait for rising edge on clock
    SBIS PIND, 0    ; Skip next instruction if PD0 is high
    RJMP LOOP       ; Jump back to LOOP if clock is low

    ; Toggle the LED on PORTC
    EOR R20, R19    ; Toggle R20 (PORTC)

    ; Jump back to LOOP
    RJMP LOOP

END_LOOP:
    ; Stop the loop
    NOP

global xpos
global ypos 
global sequence
global types
global type = left
global x = 0
global y = 0
global Array := Object()


^LButton::
MouseGetPos, xpos, ypos, id, control
text = left`t%xpos%`t%ypos%
Array.Insert(text)
return

^RButton::
MouseGetPos, xpos, ypos, id, control
text = right`t%xpos%`t%ypos%
Array.Insert(text)
return


F9:: Pause, On
F10:: Pause, Off


F3::
MsgBox x - %xpos% y - %ypos%  `n
return


F4::
b = 0
btype = 0
x = 0
y = 0
for index, element in Array ; Recommended approach in most cases.
{
	Loop, Parse, element,  %A_Tab%
		;MsgBox, %element%
	{
		;MsgBox Index - %A_Index%
		if(btype = 1)
		{
			x = %A_LoopField%
			b = 1
			btype = 0
			;MsgBox, %x%
			continue
		}
		if(b = 1)
		{
				y = %A_LoopField%
				;MouseClick, left, %x%, %y%
				b = 0
				;MsgBox, %y%
				continue
		}
		type = %A_LoopField%
		btype = 1
		;MsgBox, %type%
		continue
		

			;MsgBox, %A_LoopField%
	}
	Sleep, 1000
	b = 0
	bType = 0
			;MsgBox, %A_LoopField%
	
	MouseClick, %type%, %x%, %y%
	;Sleep, 1000
	;b = 0
	;MsgBox % "Element number " . index . " is " . element
}
return

F5::
MsgBox, %sequence%
MsgBox, %types%
return


F6::
text = left	25	45
type = Left
global x = 0
global y = 0
Loop, Parse, text, "`n"
{
	
	Loop, parse, A_LoopReadLine, %A_Tab%
	{
	;MsgBox %A_LoopField%
		if(%A_Index% = 1)
		{
				type = %A_LoopField%		
		}
		if(%A_Index% = 2)
		{
				%x%= %A_LoopField%		
		}
		if(%A_Index% = 3)
		{
				y = %A_LoopField%		
		}
		
	}
	MsgBox %type% %x% %y%
}

return















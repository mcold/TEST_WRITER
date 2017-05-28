global xpos
global ypos 
global sequence

^LButton::
LeftButton()
return

RightButton()
{
global xpos = 0
global ypos = 0
global sequence
ResultFile = result.txt
MouseGetPos, xpos, ypos, id, control
}

LeftButton()
{
ResultFile = result.txt
MouseGetPos, xwrite, ywrite, id, control
sequence .= xwrite
sequence .= "`t"
sequence .= ywrite
sequence .= "`n"

}

F9:: Pause, On
F10:: Pause, Off


F3::
MsgBox x - %xpos% y - %ypos%  `n
return


F4::
b = 0
x = 0
y = 0
Loop, Parse, sequence, `n
{
	text = %A_LoopField%
	Loop, Parse, text, %A_Tab%
	{
		MsgBox Index - %A_Index%
		if(b = 1)
		{
				y = %A_LoopField%
				MouseClick, left, %x%, %y%
				b = 0
		}
		x = %A_LoopField%
		b = 1
			;MsgBox, %A_LoopField%
	}
	Sleep, 1000
	b = 0
}

;MouseClick, left, %xpos%, %ypos%
return


F5::
MsgBox, %sequence%
return


F6::

return















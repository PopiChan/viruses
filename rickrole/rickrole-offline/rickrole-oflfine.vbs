Set WshShell = CreateObject("WScript.Shell")

WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))
WshShell.SendKeys(chr(&hAF))

Dim oPlayer
Set oPlayer = CreateObject("WMPlayer.OCX")


' Play audio
Set WshShell = CreateObject("WScript.Shell")
strCurDir = WshShell.CurrentDirectory

oPlayer.URL = strCurDir & "\rickrole.mp3"
oPlayer.controls.play 
While oPlayer.playState <> 1 ' 1 = Stopped
  WScript.Sleep 100
Wend

' Release the audio file
oPlayer.close
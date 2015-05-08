import xbmc
import xbmcgui

dialog = xbmcgui.Dialog()
i = dialog.yesno("Reset Skin Settings", "Are you sure you want to reset all skin settings? Caution, this will reset all menus, backgrounds, and widgets to their default setting.")

if i == 1:
    xbmc.executebuiltin("Skin.ResetSettings")
    xbmc.executebuiltin("Skin.SetBool(Enable.HomeDefault)")
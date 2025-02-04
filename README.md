# Slow Headed Chromium for Playwright Tests on MacOS VSCode Dev-Container

## Version 1.41

## XQuartz Setup

1. Install XQuartz (e.g. via homebrew - `brew install xquartz --cask`)
2. Restart your Mac.
3. Type on your external terminal `open -a XQuartz`.
4. On the XQuartz app go to `Preferences` Tab.
5. A window named `X11 PRefrences` will pop up, go to `Security` and press `Allow connections from network clients`.
6. Restart your Mac again and type `open -a XQuartz` on your external terminal right after.
7. Check if XQuartz is running correctly by typing `ps aux | grep Xquartz`, check to see that `/opt/X11/bin/Xquartz :0 -listen tcp` is there.
`:0` means the display is running on display port 0 Important is that it's not saying `–nolisten tcp` which would block any X11 forwarding to the X11 display.
8. Type on your external terminal `xhost +localhost`.


## VSCode Setup

1. On VS-Code - install the `Dev Containers` extension  (`"ms-vscode-remote.remote-containers"`)
2. Build the dev-container an open this repo in the container.


## Reproduction Steps

1.  Run the test `test_bbc` in headed mode, either by running `Debug Test` or, from the container terminal, running `pytest -k test_bbc --headed`
2.  To see the slow performance, switch to either the `main` or the `v1.42` branches

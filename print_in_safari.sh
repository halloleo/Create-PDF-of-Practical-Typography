open -a "Safari" "$1"
sleep 1.5
osascript -e 'tell application "Keyboard Maestro Engine" to do script "SafariPrint"'

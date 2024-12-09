package main

import (
	"syscall"
	"time"
)

var (
	user32             = syscall.NewLazyDLL("user32.dll")
	swapMouseButton    = user32.NewProc("SwapMouseButton")
	systemParametersInfo = user32.NewProc("SystemParametersInfoW")
)

const SPI_SETDESKWALLPAPER = 20

// ReverseMouse reverses the mouse buttons
func ReverseMouse() {
	swapMouseButton.Call(1)
}

// RestoreMouse restores the mouse buttons to the default state
func RestoreMouse() {
	swapMouseButton.Call(0)
}

// ChangeWallpaper sets the desktop wallpaper
func ChangeWallpaper(imagePath string) {
	systemParametersInfo.Call(
		uintptr(SPI_SETDESKWALLPAPER),
		0,
		uintptr(unsafe.Pointer(syscall.StringToUTF16Ptr(imagePath))),
		0,
	)
}

func main() {
	defer RestoreMouse()

	// Reverse mouse buttons
	ReverseMouse()

	// Set wallpaper
	imagePath := `C:\path\to\your\image.jpg`
	ChangeWallpaper(imagePath)

	// Wait for 30 seconds
	time.Sleep(30 * time.Second)
}

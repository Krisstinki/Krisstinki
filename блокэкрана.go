import (
	"os/exec"
	"log"
)

func main() {
	cmd := exec.Command("rundll32.exe", "user32.dll,LockWorkStation")
	err := cmd.Run()
	if err != nil {
		log.Fatalf("Не удалось заблокировать экран: %v", err)
	}
}


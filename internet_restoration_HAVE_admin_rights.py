import subprocess

def main():
    try:
        power_shell_command = [
            "powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-"
        ]
        
        power_shell_process = subprocess.Popen(power_shell_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        power_shell_commands = [
            "Get-NetRoute -NextHop '10.18*' | Where-Object { ($_.DestinationPrefix) -notlike '10.*' } | Remove-NetRoute -Confirm:$false -ErrorAction 'SilentlyContinue';",
            "Add-Content -Path $env:windir\\System32\\drivers\\etc\\hosts -Value \"`n45.84.154.220`tdion.vc\" -Force",
            "Add-Content -Path $env:windir\\System32\\drivers\\etc\\hosts -Value \"`n45.84.154.220`tgw.dion.vc\" -Force",
            "Add-Content -Path $env:windir\\System32\\drivers\\etc\\hosts -Value \"`n45.84.154.220`tapi-clients.dion.vc\" -Force",
            "Add-Content -Path $env:windir\\System32\\drivers\\etc\\hosts -Value \"`n45.84.154.220`tsockets-pool.dion.vc\" -Force"
        ]

        for command in power_shell_commands:
            power_shell_process.stdin.write(command + "\n")

        power_shell_process.stdin.close()

        stdout, stderr = power_shell_process.communicate()

        if stderr:
            print("Error occurred:")
            print(stderr)
        else:
            print("PowerShell commands executed successfully.")
            print("Output:")
            print(stdout)

    except subprocess.CalledProcessError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
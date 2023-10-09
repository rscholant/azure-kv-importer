import subprocess
from src.shared.utils.dates import UtilDates
from src.shared.utils.colors import bcolors


class App:
    def __init__(self, vaultName: str, envFile: str):
        self.execute(vaultName, envFile)

    def execute(self, vaultName: str, envFile: str) -> None:
        file = open(envFile, 'r')
        for line in file:
            if (line[0] != '#'):
                dates = UtilDates()
                datestart = dates.time_now()
                env = line.split('=', 1)
                print(
                    f'{datestart} - {bcolors.BLUE}IMPORTING ENV{bcolors.ENDC}: {env[0].replace("_", "-")}')
                teste = subprocess.run(
                    'az keyvault secret set --vault-name ' + vaultName + ' --name "' + env[0].replace('_', '-') + '" --value "' + env[1].replace('"', '') + '" ', shell=True, check=True, stdout=subprocess.DEVNULL)

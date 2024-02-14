import subprocess
import json
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
                if ('~>' not in line):
                    env = line.split('=', 1)
                    print(
                        f'{datestart} - {bcolors.BLUE}IMPORTING ENV{bcolors.ENDC}: {env[0].replace("_", "-")}')
                    teste = subprocess.run(
                        'az keyvault secret set --vault-name ' + vaultName + ' --name "' + env[0].replace('_', '-').rstrip('\n') + '" --value "' + env[1].replace('"', '').rstrip('\n') + '" ', shell=True, check=True, stdout=subprocess.DEVNULL)
                else:
                    env = line.split('~>', 1)
                    print(
                        f'{datestart} - {bcolors.BLUE}IMPORTING ENV{bcolors.ENDC}: {env[0].replace("_", "-")} to {env[1].replace("_", "-")}')
                    result = subprocess.run('az keyvault secret show --vault-name ' +
                                            vaultName + ' --name "' + env[0].replace('_', '-').rstrip('\n') + '"', shell=True, check=True, stdout=subprocess.PIPE)
                    subprocess.run(
                        'az keyvault secret set --vault-name ' + vaultName + ' --name "' + env[1].replace('_', '-').rstrip('\n') + '" --value "' + json.loads(result.stdout)['value'] + '" ', shell=True, check=True, stdout=subprocess.DEVNULL)

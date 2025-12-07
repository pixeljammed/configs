# milo tek - 10/07/2025 - autoexec cloner from game files
import os, shutil, json

print("pixel's half assed autoexec grabber")
print("'because it just makes sense to NOT use to use syslinks, or a bash script' -me 2025")
print("---------------------------------------------------------------------------")
print("put your paths to autoexecs in autoexecs.json")
print("starting...")

def snatch(files):
    with open(files, "r") as f:
        data = json.load(f)

    games = list(data["gameconfigs"].keys())
    for game in games:
        try:
            os.mkdir(game)
        except Exception as e:
            print(f"error making {game} folder: {e}")
            pass
        configs = data["gameconfigs"][game]
        for config in configs:
            try:
                shutil.copy(config, game)
                print(f"copied {game} cfg {config} file succesfully")
            except Exception as e:
                print(f"error copying {game} cfg '{config}' file: {e}")

snatch("autoexecs.json")

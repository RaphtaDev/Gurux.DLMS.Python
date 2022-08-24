import requests


def scrap_units(file_name="logFile.txt"):
    try:
        with open(file_name) as log_file:
            # improved the perfoamnce by reducing the iterrations from 183 to 3
            for line in reversed(log_file.readlines()):
                if "Index" in line:
                    value_line = line.strip()
                    units_list = value_line.split(":")
                    units_str = units_list[2]
                    units = int(units_str.strip())
                    return {"status": "success", "payload": units}
            return {"status": "error", "payload": "No units found"}
    except Exception as e:
        return {"status": "error", "payload": e}


def upload_units(units):
    try:
        url = "http://164.92.174.48:800/api/operations/meterreading"
        myobj = {"meter": 1, "reading": units}
        x = requests.post(url, json=myobj)
        return x.json()
    except Exception as e:
        return {"exception": e}


if __name__ == "__main__":
    scrap_result = scrap_units()
    if scrap_result["status"] == "success":
        units = scrap_result["payload"]
        response = upload_units(units)
        print(response)
    elif scrap_result["status"] == "error":
        print(scrap_result["payload"])
    else:
        print(scrap_result["payload"])

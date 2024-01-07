import subprocess
import platform
import json

def conduct_compliance_check():
    # Get the macOS version
    macos_version = platform.mac_ver()[0]
    print("macOS version: {}".format(macos_version))
    if macos_version >= "10.15":
        print("macOS version is 10.15 or above, proceeding with compliance check")
        json_file = "macOS_" + macos_version.split(':')[0][:2] + ".json"
        passed, failed, NUMBER_OF_CHECKS = read_json(json_file)

    print("\nCompliance check completed")
    print(25*"*")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Total: {NUMBER_OF_CHECKS}")
    print(f"Compliance check percentage: {passed/NUMBER_OF_CHECKS*100}")

def read_json(json_file):
    # Read the json file
    path = "benchmarks/" + json_file
    with open(path, 'r') as f:
        compliance = json.load(f)
    
    NUMBER_OF_CHECKS = len(compliance['cis_benchmarks'])
    passed_checks = 0
    failed_checks = 0
    
    print("Compliance check started")
    print(25*"*")
    # Iterate through the dictionary
    checks = compliance['cis_benchmarks']

    for check in checks:
        print(f"\n{check['test_id']} - {check['test_name']}")
        print(25*"-")
        print(f"{check['description']}\n")
        print(f"\nExpected Result: {check['outcome']}")
        actual_result = subprocess.run(check['command'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"\nActual Result: {actual_result.stdout.decode('utf-8')}")


    return passed_checks, failed_checks, NUMBER_OF_CHECKS

if __name__ == "__main__":
    conduct_compliance_check()
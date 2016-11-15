import requests

url = "http://agl-developer-test.azurewebsites.net/people.json"


def main():
    url = "http://agl-developer-test.azurewebsites.net/people.json"
    female = []
    male = []
    response = requests.get(url)
    data = response.json()
    # print(len(data))

    for i in range(len(data)):
        if data[i]['pets'] is not None:
            gender = data[i]['gender']
            for j in range(len(data[i]['pets'])):
                if gender == "Male" and data[i]['pets'][j]['type'] == "Cat":
                    male.append(data[i]['pets'][j]['name'])
                elif gender == "Female" and data[i]['pets'][j]['type'] == "Cat":
                    female.append(data[i]['pets'][j]['name'])
                else:
                    pass
        else:
            pass

    male.sort()
    female.sort()
    print("Male: \n")
    for _ in range(len(male)):
        print(male[_])
    print("\nFemale: \n")
    for _ in range(len(female)):
        print(female[_])


# print(data[0]['pets'][1]['name'])
# request.release_conn()

if __name__ == "__main__":
    main()

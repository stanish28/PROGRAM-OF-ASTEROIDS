import requests
print("")
print("The difference between the start and the end dates must be seven days and not more than that")
print("")
start_date = input("Enter the start Date in the format (YYYY-MM-DD):   ")
end_date = input("Enter the end Date in the format   (YYYY-MM-DD):   ")

url = "https://api.nasa.gov/neo/rest/v1/feed?start_date={}&end_date={}&api_key=DEMO_KEY".format(start_date, end_date)
response = requests.get(url)
read_data = response.json()

print("No.of asteroids passing between the dates given are:", end=" ")

for i in read_data.keys():
    if i == "element_count":
        print(read_data.get(i))
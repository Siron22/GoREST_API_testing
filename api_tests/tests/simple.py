import requests

url = 'https://gorest.co.in/public/v2/users'
post_data = {
        "title": "Cumque voluptas ut dolor laboriosam praesentium temporibus dolores iste doloribus.",
        "body": "Aliquam est quis nostrum nostrum consequatur beatae.Illo et nihil. Quia sunt alias et et."
        }
headers = { "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer 0c59c9b43ae6904c1cfcd0b5e92477eaea748750f6e39db52d099cff8450430c"}

response = requests.get(url, headers=headers)
a = {'id': 495843, 'name': 'Gautama Asan', 'email': 'gautama_asan@kuhn-hyatt.info', 'gender': 'female', 'status': 'active'}


print(a in response.json())

response = [
    {
        "id": 20052,
        "user_id": 492320,
        "title": "Et minus illum provident officia omnis nostrum odit dolore.",
        "body": "Laboriosam dolor ratione officia. Laudantium illum non facilis autem. Ut magnam omnis iste ut quidem optio quod est."
    },
    {
        "id": 20051,
        "user_id": 492320,
        "title": "Sint qui amet.",
        "body": "Odit consectetur quod quis corporis. Voluptates architecto sunt. Temporibus aut maiores qui rerum sint odit. Voluptatum aliquam nisi asperiores autem qui voluptate quidem. Soluta aut est consectetur voluptatibus dolores est."
    },
    {
        "id": 20050,
        "user_id": 492320,
        "title": "A voluptas optio possimus doloribus sapiente consequuntur.",
        "body": "Porro sit nulla voluptas ut in dolor ut iste ut. Quae nostrum necessitatibus unde minus autem sunt numquam et. Ut quo quisquam sunt voluptatum id dolorem. Id magni est quod facere."
    },
    {
        "id": 20027,
        "user_id": 492320,
        "title": "Eius ut sequi eum tempore libero repellendus similique quia repudiandae.",
        "body": "Magnam velit facilis et eligendi dolores qui. Et natus rem earum atque voluptatem. Delectus aut sint porro ut cum illum magnam. Natus quis provident. Omnis reiciendis asperiores et."
    }
]

post = {
    "id": 20052,
    "user_id": 492320,
    "title": "Et minus illum provident officia omnis nostrum odit dolore.",
    "body": "Laboriosam dolor ratione officia. Laudantium illum non facilis autem. Ut magnam omnis iste ut quidem optio quod est."
}

# print(post in response)
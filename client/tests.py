# from django.test import TestCase
# from django.urls import reverse
# from django.contrib.auth import get_user_model
# from .models import Client
# from rest_framework.test import APITestCase
# from rest_framework import status
# # # Create your tests here.


# class ClientTest(APITestCase):

#     @classmethod
#     def setUpTestData(cls):
#         testuser1 = get_user_model().objects.create_user(
#             username="testuser1", password="pass"
#         )
#         testuser1.save()

#         testuser2 = get_user_model().objects.create_user(
#             username="testuser2", password="pass"
#         )
#         testuser2.save()

#         test_client = Client.objects.create(
#             owner=testuser1,
#             Name="user1",
#             Mobile="079",
#             Email="user1@client.com",
#             Country="jordan",
#             City="amman",
#             Date_of_Birth="2023-02-06",
#             Contract_Start_Date="2023-02-06",
#             Contract_End_Date="2023-02-06",
#             Status='Active'

#         )
#         test_client.save()

#         test_Client2 = Client.objects.create(
#             owner=testuser1,
#             Name="user2",
#             Mobile="079",
#             Email="user2@client.com",
#             Country="jordan",
#             City="amman",
#             Date_of_Birth="1993-08-06",
#             Contract_Start_Date="2020-02-06",
#             Contract_End_Date="2023-02-06",
#             Status='not Active'
#         )
#         test_Client2.save()

#         test_Client3 = Client.objects.create(
#             owner=testuser2,
#             Name="user3",
#             Mobile="079",
#             Email="user3@client.com",
#             Country="jordan",
#             City="amman",
#             Date_of_Birth="1980-11-06",
#             Contract_Start_Date="2011-02-06",
#             Contract_End_Date="2023-02-06",
#             Status='Active'
#         )
#         test_Client3.save()

#     def setUp(self):
#         self.client.login(username='testuser2', password="pass")

#     def test_client_model(self):
#         client = Client.objects.get(id=3)
#         actual_owner = str(client.owner)
#         actual_name = str(client.type)

#         self.assertEqual(actual_owner, "testuser2")
#         self.assertEqual(actual_name, "user3")


#     def test_user1_get_all_clients(self):
#         self.client.logout()
#         self.client.login(username='testuser1', password="pass")
#         url = reverse("client_list")
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         client = response.data
#         self.assertEqual(len(client), 3)

from card.models import Card

from .test_setup import TestSetUp


class TestViews(TestSetUp):
    def test_user_can_get_items_in_card(self):
        card_instance = Card.objects.create(name="test")

        request = self.client.get(self.end_points['card'])
        recieved_numbers = request.data

        self.assertEqual(
            card_instance.name, recieved_numbers[0]['name'], "user can't get items list")
        self.assertEqual(request.status_code, 200, "user can't get items list")

    def test_user_can_add_item_to_card(self):
        request = self.client.post(self.end_points['card'], {'name': 'test'})

        self.assert_(Card.objects.filter(name="test").exists(),
                     "user can't add item to card")
        self.assertEqual(request.status_code, 200,
                         "user can't add item to card")

    def test_user_can_update_item_in_card(self):
        card_instance = Card.objects.create(name="test")

        request = self.client.put(
            self.end_points['card'] + "1", {'name': 'test 2'})
        self.assert_(Card.objects.filter(name="test 2").exists(),
                     "user can't update item in card")
        self.assertEqual(request.status_code, 202,
                         "user can't update item in card")

    def test_user_can_remove_item_from_card(self):
        Card.objects.create(name="test")
        request = self.client.delete(self.end_points['card'] + "1")

        self.assertFalse(Card.objects.filter(
            name="test 2").exists(), "user can't delete an item")
        self.assertEqual(request.status_code, 200,
                         "user can't remove item from card")

import random
from django.test import TestCase
from .models import Player


class PlayerModelUnitTestCase(TestCase):
    def setUp(self):
        self.player = Player.objects.create(
            player_number=random.randint(10000, 99999),
            first_name='Bob',
            last_name='Smith',
            email='bob.smith@test.com',
            role='Leg-Spin Bowler',
            subscription='Paid'
        )

    def test_player_model(self):
        data = self.player
        self.assertIsInstance(data, Player)

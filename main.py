import player as p
import game as g


print("Player 1")
p1 = p.Player(9, 3).card_making()
player_1, player_1_list = p1[0], p1[1]
print(player_1)

print("\nPlayer 2")
p2 = p.Player(9, 3).card_making()
player_2, player_2_list = p2[0], p2[1]
print(player_2)

bag = 100  # 100 kegs to be withdrawn
print("\n")
loto = g.Play(bag, player_1, player_2, player_1_list, player_2_list)
loto.play()

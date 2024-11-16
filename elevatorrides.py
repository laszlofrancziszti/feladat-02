# --------------------------------------------------megoldás---------------------------------------
def min_elevator_rides(n, x, weights):
    dp = [(n + 1, 0)] * (1 << n)  # (szükséges utak, utolsó út súlya)
    dp[0] = (1, 0)

    for mask in range(1 << n):
        for i in range(n):
            if mask & (1 << i) == 0:  # ha az i-edik személy nincs a mask-ban
                new_mask = mask | (1 << i)
                rides, last_weight = dp[mask]
                # Ha az i-edik személy befér az utolsó útra
                if last_weight + weights[i] <= x:
                    new_rides = (rides, last_weight + weights[i])
                else:
                    # Új utat kell kezdenünk
                    new_rides = (rides + 1, weights[i])
                # Frissítjük a dp-t, ha kevesebb útra van szükség
                dp[new_mask] = min(dp[new_mask], new_rides)

    return dp[(1 << n) - 1][0]


# -----------------------------------------------teszt-------------------------------------------
print(min_elevator_rides(2, 10, [5, 5]))  # Elvárt eredmény: 1
print(min_elevator_rides(3, 10, [4, 4, 4]))  # Elvárt eredmény: 2
print(min_elevator_rides(4, 10, [4, 8, 6, 1]))  # Elvárt eredmény: 2
print(min_elevator_rides(5, 15, [7, 8, 4, 5, 6]))  # Elvárt eredmény: 3
print(min_elevator_rides(3, 6, [5, 3, 2]))  # Elvárt eredmény: 2
print(min_elevator_rides(6, 20, [10, 10, 10, 10, 10, 10]))  # Elvárt eredmény: 3
print(min_elevator_rides(4, 12, [4, 5, 7, 6]))  # Elvárt eredmény: 2
print(min_elevator_rides(5, 25, [12, 8, 7, 8, 5]))  # Elvárt eredmény: 2
print(min_elevator_rides(3, 15, [5, 10, 5]))  # Elvárt eredmény: 1
print(
    min_elevator_rides(10, 50, [10, 15, 20, 5, 10, 15, 20, 5, 10, 15])
)  # Elvárt eredmény: 5

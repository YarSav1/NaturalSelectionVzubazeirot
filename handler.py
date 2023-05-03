import random

from config import commandsCount, commandsCountMassive, commandsCountMassiveCoordinates, field, blockCount, start


def _handler():
    global field, commandsCountMassiveCoordinates, commandsCountMassive, start
    # print(commandsCount)

    for i in range(commandsCount):
        end = False
        cikl = 0
        command_coordinates = commandsCountMassiveCoordinates[i]
        len_command_coordinates = 4
        if len(command_coordinates) > len_command_coordinates:
            len_command_coordinates = len(command_coordinates)

        # Раздача подарков всем в одной команде, ну почти всем
        for j in range(random.randint(0, len_command_coordinates)):
            try:
                random_cell = random.choice(command_coordinates)
            except Exception as exc:
                break
            field[random_cell[0]][random_cell[1]][3] += random.randint(0, 10)

        remains_cikl = int(len_command_coordinates / 100 * 10)
        if remains_cikl < 3:
            remains_cikl = 3

        while end is False:

            if cikl == remains_cikl:
                break
            command = commandsCountMassive[i]
            command_coordinates = commandsCountMassiveCoordinates[i]
            # print(f'Индекс - {i} - Ячеек: {len(commandCoordinates)}\n'
            #       f'{commandCoordinates}')
            # print(commandsCountMassiveCoordinates[0])

            free_cell = []
            for coord in command_coordinates:
                vrag = 0
                drug = 0
                # print(f'Ячейка - {field[coord[0]][coord[1]]}')
                # field[coord[0]][coord[1]][3] += random.randint(0, 15000)
                if coord[0] < blockCount - 1:
                    if [field[coord[0] + 1][coord[1]][0], field[coord[0] + 1][coord[1]][1],
                        field[coord[0] + 1][coord[1]][2]] != command:
                        pass
                    else:
                        drug += 1
                if coord[0] != 0:
                    if [field[coord[0] - 1][coord[1]][0], field[coord[0] - 1][coord[1]][1],
                        field[coord[0] - 1][coord[1]][2]] != command:
                        pass
                    else:
                        drug += 1
                if coord[1] != 0:
                    if [field[coord[0]][coord[1] - 1][0], field[coord[0]][coord[1] - 1][1],
                        field[coord[0]][coord[1] - 1][2]] != command:
                        pass
                    else:
                        drug += 1
                if coord[1] < blockCount - 1:
                    if [field[coord[0]][coord[1] + 1][0], field[coord[0]][coord[1] + 1][1],
                        field[coord[0]][coord[1] + 1][2]] != command:
                        pass
                    else:
                        drug += 1

                # if start2 is True:
                #     free_cell.append(coord)

                if coord[0] < blockCount - 1:
                    if coord[1] < blockCount - 1:
                        if [field[coord[0] + 1][coord[1] + 1][0], field[coord[0] + 1][coord[1] + 1][1],
                            field[coord[0] + 1][coord[1] + 1][2]] != command:
                            pass
                        else:
                            drug += 1
                if coord[0] < blockCount - 1:
                    if coord[1] != 0:
                        if [field[coord[0] + 1][coord[1] - 1][0], field[coord[0] + 1][coord[1] - 1][1],
                            field[coord[0] + 1][coord[1] - 1][2]] != command:
                            pass
                        else:
                            drug += 1
                if coord[0] != 0:
                    if coord[1] < blockCount - 1:
                        if [field[coord[0] - 1][coord[1] + 1][0], field[coord[0] - 1][coord[1] + 1][1],
                            field[coord[0] - 1][coord[1] + 1][2]] != command:
                            pass
                        else:
                            drug += 1
                if coord[0] != 0:
                    if coord[1] != 0:
                        if [field[coord[0] - 1][coord[1] - 1][0], field[coord[0] - 1][coord[1] - 1][1],
                            field[coord[0] - 1][coord[1] - 1][2]] != command:
                            pass
                        else:
                            drug += 1
                # print(drug)
                if drug >= 5:
                    free_cell.append(coord)
                elif start != 0:
                    free_cell.append(coord)

            if len(free_cell) != 0:
                catch_cell = random.choice(free_cell)
                power_cell_catch = field[catch_cell[0]][catch_cell[1]][3]
                attacking_cell = []
                if catch_cell[0] < blockCount - 1:
                    if [field[catch_cell[0] + 1][catch_cell[1]][0], field[catch_cell[0] + 1][catch_cell[1]][1],
                        field[catch_cell[0] + 1][catch_cell[1]][2]] != command:
                        if field[catch_cell[0] + 1][catch_cell[1]] not in attacking_cell:
                            attacking_cell.append([catch_cell[0] + 1, catch_cell[1]])
                if catch_cell[0] != 0:
                    if [field[catch_cell[0] - 1][catch_cell[1]][0], field[catch_cell[0] - 1][catch_cell[1]][1],
                        field[catch_cell[0] - 1][catch_cell[1]][2]] != command:
                        if field[catch_cell[0] - 1][catch_cell[1]] not in attacking_cell:
                            attacking_cell.append([catch_cell[0] - 1, catch_cell[1]])
                if catch_cell[1] != 0:
                    if [field[catch_cell[0]][catch_cell[1] - 1][0], field[catch_cell[0]][catch_cell[1] - 1][1],
                        field[catch_cell[0]][catch_cell[1] - 1][2]] != command:
                        if field[catch_cell[0]][catch_cell[1] - 1] not in attacking_cell:
                            attacking_cell.append([catch_cell[0], catch_cell[1] - 1])
                if catch_cell[1] < blockCount - 1:
                    if [field[catch_cell[0]][catch_cell[1] + 1][0], field[catch_cell[0]][catch_cell[1] + 1][1],
                        field[catch_cell[0]][catch_cell[1] + 1][2]] != command:
                        if field[catch_cell[0]][catch_cell[1] + 1] not in attacking_cell:
                            attacking_cell.append([catch_cell[0], catch_cell[1] + 1])
                # if catch_cell[0] < blockCount - 1:
                #     if catch_cell[1] < blockCount - 1:
                #         if field[catch_cell[0] + 1][catch_cell[1] + 1] != command and field[catch_cell[0] + 1][
                #             catch_cell[1] + 1] not in attacking_cell:
                #             attacking_cell.append([catch_cell[0] + 1, catch_cell[1] + 1])
                # if catch_cell[0] < blockCount - 1:
                #     if catch_cell[1] != 0:
                #         if field[catch_cell[0] + 1][catch_cell[1] - 1] != command and field[catch_cell[0] + 1][
                #             catch_cell[1] - 1] not in attacking_cell:
                #             attacking_cell.append([catch_cell[0] + 1, catch_cell[1] - 1])
                # if catch_cell[0] != 0:
                #     if catch_cell[1] < blockCount - 1:
                #         if field[catch_cell[0] - 1][catch_cell[1] + 1] != command and field[catch_cell[0] - 1][
                #             catch_cell[1] + 1] not in attacking_cell:
                #             attacking_cell.append([catch_cell[0] - 1, catch_cell[1] + 1])
                # if catch_cell[0] != 0:
                #     if catch_cell[1] != 0:
                #         if field[catch_cell[0] - 1][catch_cell[1 - 1]] != command and field[catch_cell[0] - 1][
                #             catch_cell[1 - 1]] not in attacking_cell:
                #             attacking_cell.append([catch_cell[0] - 1, catch_cell[1] - 1])
                if len(attacking_cell) != 0:
                    attacking_cell = random.choice(attacking_cell)
                    # print(attacking_cell)

                    power_cell_attacking = field[attacking_cell[0]][attacking_cell[1]][3]

                    # print(f'{catch_cell} - {attacking_cell}')
                    # print(f'{power_cell_catch} - {power_cell_attacking}')
                    # surprise = power_cell_catch // 100 * 200
                    if power_cell_catch >= power_cell_attacking + power_cell_attacking / 100 * 50:
                        # print(f'Атака - {attacking_cell}')

                        remains_power = int((power_cell_catch + power_cell_attacking) / 2)

                        field[attacking_cell[0]][attacking_cell[1]] = [field[catch_cell[0]][catch_cell[1]][0],
                                                                       field[catch_cell[0]][catch_cell[1]][1],
                                                                       field[catch_cell[0]][catch_cell[1]][2],
                                                                       power_cell_catch + remains_power]
                        field[catch_cell[0]][catch_cell[1]] = [field[catch_cell[0]][catch_cell[1]][0],
                                                               field[catch_cell[0]][catch_cell[1]][1],
                                                               field[catch_cell[0]][catch_cell[1]][2],
                                                               power_cell_attacking + remains_power]


                        for g in range(commandsCount):
                            if commandsCountMassiveCoordinates[g] != i:
                                if attacking_cell in commandsCountMassiveCoordinates[g]:
                                    # print(commandsCountMassiveCoordinates[g])
                                    commandsCountMassiveCoordinates[g].remove(attacking_cell)
                                    # print(commandsCountMassiveCoordinates[g])
                                    # print('\n')
                                    # print('Удалено')
                                    # if len(commandsCountMassiveCoordinates[g]) == 0:
                                    # commandsCountMassiveCoordinates.remove(g)
                                    # commandsCountMassive.pop(g)

                        commandsCountMassiveCoordinates[i] += [attacking_cell]
                        end = True
                    else:
                        cikl += 1
                else:
                    end = True
            else:
                end = True
    if start != 0:
        start -= 1

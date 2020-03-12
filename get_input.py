def get_input(filename):
    with open(filename, 'r') as f:
        w, h = f.readline().split()
        w, h = int(w), int(h)
        office_map = [f.readline()[:-1] for _ in range(h)]

        num_devel = int(f.readline())
        developer_list = []
        for _ in range(num_devel):
            company, bonus, _, *skillset = f.readline().split()
            developer_list.append([company, int(bonus), set(skillset)])

        num_managers = int(f.readline())
        manager_list = []
        for _ in range(num_managers):
            company, bonus = f.readline().split()
            manager_list.append([company, int(bonus)])
        return office_map, developer_list, manager_list 
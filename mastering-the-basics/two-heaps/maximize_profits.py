
def maximize_capital(n, k, c, capitals, profits):
    number_of_projects = n
    max_projects_allowed = k
    initial_capital = c
    
    cumulative_capital = initial_capital
    selected_project_indexes = set()

    for _ in range(max_projects_allowed):
        # Select a project

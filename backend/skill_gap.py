def find_missing_skills(user_skills, required_skills):

    user_set = set(
        user_skills.lower().split()
    )

    required_set = set(
        required_skills.lower().split()
    )

    missing = required_set - user_set

    return list(missing)    
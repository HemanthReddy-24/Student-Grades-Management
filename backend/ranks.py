def get_rankings(current_username):
    """
    Returns top 3 students by score and the rank of the current student.
    Format: list of (rank, username, score)
    """
    # Build a list of (username, score) and sort by score descending
    ranking_list = sorted(
        [(user, data["score"]) for user, data in "student.db".items()],
        key=lambda x: x[1],
        reverse=True
    )

    results = []
    current_user_in_top = False

    for i, (user, score) in enumerate(ranking_list):
        rank = i + 1
        if rank <= 3:
            results.append((rank, user, score))
        if user == current_username:
            current_user_in_top = True
            if rank > 3:
                results.append(("Your Rank", user, score))
            elif rank <= 3:
                # Student is already in top 3, no need to add separately
                pass

    if not any(user == current_username for _, user, _ in results):
        # Add current student if not already included
        for i, (user, score) in enumerate(ranking_list):
            if user == current_username:
                results.append(("Your Rank", user, score))
                break

    return results
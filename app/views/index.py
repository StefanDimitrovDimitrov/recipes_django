from django.shortcuts import render


def index(request):
    return render(request, 'index.html')





# def index(request):
#     if Profile.objects.exists():
#         profile = get_profile()
#         expenses = Expense.objects.all()
#
#         profile.budget_left = calculate_budget_left(profile, expenses)
#
#         context = {
#             'profile': profile,
#             'expenses': expenses,
#         }
#
#         return render(request, 'home-with-profile.html', context)
#     else:
#         return create_profile(request)

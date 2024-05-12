#include <iostream>
#include <cstdlib>
#include <vector>

int evaluation_function(std::vector<int> f)
{
    srand((unsigned)time(NULL));
    int random = rand() % 101;
    std::cout << random << "\n";
    return random;
}

void greedy_forward(std::vector<int> f)
{

    int max_accuracy = -1;
    int temp_accuracy = 0;
    int index_of_best = -1;
    while (temp_accuracy >= max_accuracy)
    {
    }
}

void greedy_backwards(std::vector<int> f)
{
    int max_accuracy = -1;
    int temp_accuracy = 0;
    int index_of_best = -1;
    while (temp_accuracy >= max_accuracy)
    {
    }
}

int main()
{
    int feature_count;
    int algo_input;
    std::vector<int> features;

    std::cout << "Please enter the number of features: /n";
    std::cin >> feature_count;
    for (int i = 0; i < feature_count; i++)
    {
        features.push_back(i);
    }
    std::cout << "1. Greedy Forwards\n 2. Greedy Backwards\n Please enter the number of the algorithm you would like to use:\n";
    std::cin >> algo_input;
    if (algo_input == 0)
    {
        greedy_forward(features);
    }
    else
    {
        greedy_backwards(features);
    }
    return 0;
}
#include <iostream>
#include <cstdlib>
#include <vector>
#include <ctime>

int evaluate(std::vector<int> f)
{
    int random = rand() % 101;
    return random;
}

void print_state(std::vector<int> s)
{
    for (int i = 0; i < s.size(); i++)
    {
        std::cout << s.at(i);
        if (i + 1 < s.size())
        {
            std::cout << ", ";
        }
    }
}

void greedy_forward(std::vector<int> f)
{

    int max_accuracy = 0;
    int current_accuracy = 0;
    int temp_accuracy = 0;
    int index_of_best = 0;
    std::vector<int> initial_state;
    std::vector<int> options = f;
    std::vector<int> temp;
    std::vector<std::vector<int>> queue;

    max_accuracy = evaluate(initial_state);

    std::cout << "Using no features and “random” evaluation, I get an accuracy of " << max_accuracy << "%\n\n";

    for (int i = 0; i < f.size(); i++)
    {
        temp.push_back(f.at(i));
        queue.push_back(temp);
        temp.clear();
    }

    int max_number_of_features = f.size() + 1;

    std::cout << "Beginning search.\n\n";

    for (int k = 0; k < max_number_of_features; k++)
    {
        if (k > 0)
        { // set up queue of feature combinations to be tested
            queue.clear();
            for (int i = 0; i < options.size(); i++)
            {
                temp = initial_state;
                temp.push_back(options.at(i));
                queue.push_back(temp);
            }
        }
        // check if each element in queue is
        for (int i = 0; i < queue.size(); i++)
        {
            temp_accuracy = evaluate(queue.at(i));
            std::cout << "\tUsing feature(s) {";
            print_state(queue.at(i));
            std::cout << "} accuracy is " << temp_accuracy << "%\n";
            if (temp_accuracy >= current_accuracy)
            {
                index_of_best = i;
                current_accuracy = temp_accuracy;
            }
        }

        if (current_accuracy >= max_accuracy)
        {
            initial_state.clear();
            initial_state = queue.at(index_of_best);
            options.erase(options.begin() + index_of_best);
            max_accuracy = current_accuracy;
            current_accuracy = 0;
            std::cout << "\nFeature set {";
            print_state(initial_state);
            std::cout << "} was best, accuracy is " << max_accuracy << "%\n\n";
        }
        else
        {
            std::cout << "\n(WARNING ACCURACY REDUCED)\n\n";
            k = max_number_of_features; // break out of for loop
        }
    }

    std::cout << "Finished search!! The best feature subset is {";
    print_state(initial_state);
    std::cout << "} , which has an accuracy of " << max_accuracy << "%\n\n";
}

void greedy_backwards(std::vector<int> f)
{

    int max_accuracy = 0;
    int current_accuracy = 0;
    int temp_accuracy = 0;
    int index_of_best = 0;
    std::vector<int> initial_state = f;
    std::vector<int> temp;
    std::vector<std::vector<int>> queue;

    queue.push_back(initial_state);

    int max_number_of_features = f.size() + 1;

    std::cout << "Beginning search.\n\n";

    for (int k = 0; k < max_number_of_features; k++)
    {
        if (k > 0)
        { // set up queue of feature combinations to be tested
            queue.clear();
            for (int i = 0; i < initial_state.size(); i++)
            {
                temp = initial_state;
                temp.erase(temp.begin() + i);
                queue.push_back(temp);
            }
        }
        // check if each element in queue is
        for (int i = 0; i < queue.size(); i++)
        {
            temp_accuracy = evaluate(queue.at(i));
            std::cout << "\tUsing feature(s) {";
            print_state(queue.at(i));
            std::cout << "} accuracy is " << temp_accuracy << "%\n";
            if (temp_accuracy >= current_accuracy)
            {
                index_of_best = i;
                current_accuracy = temp_accuracy;
            }
        }

        if (current_accuracy >= max_accuracy)
        {
            initial_state.clear();
            initial_state = queue.at(index_of_best);
            max_accuracy = current_accuracy;
            current_accuracy = 0;
            std::cout << "\nFeature set {";
            print_state(initial_state);
            std::cout << "} was best, accuracy is " << max_accuracy << "%\n\n";
        }
        else
        {
            std::cout << "\n(WARNING ACCURACY REDUCED)\n\n";
            k = max_number_of_features; // break out of for loop
        }
    }

    std::cout << "Finished search!! The best feature subset is {";
    print_state(initial_state);
    std::cout << "} , which has an accuracy of " << max_accuracy << "%\n\n";
}

int main()
{
    srand(static_cast<unsigned>(time(nullptr)));
    int feature_count;
    int algo_input;
    std::vector<int> features;
    std::cout << "Welcome to Rachel Danover's Feature Selection Algorithm.\n\n";
    std::cout << "Please enter the number of features: \n";
    std::cin >> feature_count;
    for (int i = 0; i < feature_count; i++)
    {
        features.push_back(i + 1);
    }

    std::cout << "1. Greedy Forwards\n2. Greedy Backwards\nPlease enter the number of the algorithm you would like to use or 0 to quit:\n";
    std::cin >> algo_input;
    if (algo_input == 1)
    {
        greedy_forward(features);
    }
    else if (algo_input == 2)
    {
        greedy_backwards(features);
    }

    return 0;
}
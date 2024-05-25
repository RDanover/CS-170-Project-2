/*
TBD:

- normalize test data in train
- implement test
- implement evaluate
- allow user input for feature choice??

*/

#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

std::vector<std::vector<double>> raw_data;

void train(std::string filename)
{
    std::ifstream file(filename);
    std::string line;

    if (!file.is_open())
    {
        std::cout << "Error opening file: " << filename << "\n";
    }
    int num_rows = 0;
    while (getline(file, line))
    {
        std::stringstream ss(line);
        std::string value;
        std::vector<double> row;
        int num_columns = 0;
        while (ss >> value)
        {
            num_columns++;
            row.push_back(stod(value));
        }
        num_rows++;
        raw_data.push_back(row);
    }

    file.close();

    // file has been placed into data

    std::vector<double> columns;

    for (int i = 0; i < num_columns; i++)
    {
        columns.push_back(0);
    }

    for (int r = 0; r < raw_data.size(); r++)
    {

        for (int c = 0; c < raw_data.at(r).size(); c++)
        {
            columns.at(c) += raw_data.at(r).at(c);
        }
    }

    for (int i = 0; i < num_columns; i++)
    {
        columns.at(i) /= num_rows; // columns now stores averages of each column
    }

    for (int r = 0; r < raw_data.size(); r++)
    {
        for (int c = 0; c < raw_data.at(r).size(); c++)
        {
            
        }
    }

    // normalize data
}

void test(std::vector<double> test_case, int index_of_test_case, std::vector<int> feature_indexes)
{
    // itterate through training data calculate euclidean distance for each, excluding the test case
    // sort from greatest - > least
    // pick top classsifier
}

double evaluate(std::vector<int> feature_indexes)
{
    // use leave one out validator calling the test function for each itteration (aka row)
    // return num correct/ total itterations
    return -1;
}

int main(int argc, char *argv[])
{
    int feature_count = 0;
    int feature = 0;
    std::vector<int> features;

    if (argc != 2)
    {
        std::cout << "Please provide input file.\n";
        return 1;
    }
    std::string filename = argv[1];

    train(filename);

    std::cout << "Please enter the number of features: \n";

    std::cin >> feature_count;

    std::cout << "Please enter the indexes of the features you would like to use:\n";

    for (int i = 0; i < feature_count; i++)
    {
        std::cin >> feature;
        features.push_back(feature);
    }

    return 0;
}

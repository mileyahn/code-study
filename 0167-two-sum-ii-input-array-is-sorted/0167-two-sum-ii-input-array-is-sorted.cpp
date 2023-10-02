class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> output;
        int i = 0;
        int j = numbers.size()-1;
        while(j > i){
            int add = numbers[i] + numbers[j];
            if(add > target){
                j--;
            }else if(add == target){
                output.push_back(i+1);
                output.push_back(j+1);
                break;
            }else{
                i++;
            }
        }
        return output;
    }
};
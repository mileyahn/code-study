class Solution {
public:
    int maxArea(vector<int>& height) {
        int i = 0;
        int j = height.size()-1;
        int max = 0;
        while(i < j){
            int amount = (j-i) * min(height[i], height[j]);
            if(amount > max){
                max = amount;
            }
            if(height[i] < height[j]) i++;
            else if(height[j] < height[i]) j--;
            else{
                i++;
                j--;
            }
        }
        return max;
    }
};
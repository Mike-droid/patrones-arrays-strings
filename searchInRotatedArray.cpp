#include <vector>
int searchInRotatedArray(vector<int> &nums, int target) {
  int izquierda = 0;
  int derecha = nums.size() - 1;
  int mitad;

  while (izquierda <= derecha) {
    mitad = izquierda + (derecha - izquierda) / 2;
    if (nums[mitad] == target) {
      return mitad;
    }
    if (nums[mitad] >= nums[izquierda]) {
      if (target >= nums[izquierda] && target < nums[mitad]) {
        derecha = mitad - 1;
      } else {
        izquierda = mitad + 1;
      }
    } else {
      if (target > nums[mitad] && target <= nums[derecha]) {
        izquierda = mitad + 1;
      } else {
        derecha = mitad - 1;
      }
    }
  }

  return -1;
}
def get_min_capacity():
    min_difference = float("inf")
    min_capacity = float("inf") # Başlangıçta minimum kapasite sonsuz olarak tanımlanır
    object_volumes = [1.1,1.2,3.5,4.6,8.9,9] 
    for height_split_nums in range(2,11): 
        height_nums = np.linspace(0, 10, num=height_split_nums)
        for width_split_nums in range(2,11):
            width_nums = np.linspace(0, 10, num=width_split_nums)
            for length_split_nums in range(2,11):
                length_nums = np.linspace(0, 10, num=length_split_nums)

                # Tüm kombinasyonlar için toplam kapasite hesaplanır ve minimum kapasite güncellenir
              
        
                w = width_nums[1]-width_nums[0]
                h = height_nums[1]-height_nums[0]
                l = length_nums[1]-length_nums[0]
                capacity = w * h * l
                difference = abs(sum(object_volumes) - capacity)
                if difference < min_difference:
                    min_difference = difference
                    if (len([col for col in object_volumes if col<=capacity])==len(object_volumes) and (capacity < min_capacity)):
                        min_capacity=capacity  
    return min_capacity,w,h,l,height_split_nums,width_split_nums,length_split_nums
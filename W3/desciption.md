## 1. Ý tưởng thực hiện
# 1.1 Gauss - Jordan
Ta thực hiện giống như Guass Jordan.
Thay đổi ở chỗ : bước chuẩn hóa cột : thay vì chỉ chuẩn hóa cột ở các hàng ở dưới hàng đang xét về 0,ta làm cả các cột phía trên hàng đang xét(không chuẩn hóa cột đang xét).

# 1.2 Tìm ma trận khả nghịch
1. Lấy số dòng và cột cho biến m,n
2. Nếu m = n thì tiếp tục, không thì trả về 0 vì chỉ có ma trận vuông mới khả nghịch
3. Tạo ra ma trận đơn vị I với độ lớn n*n
4. Gộp ma trận I với ma trận ban đầu A tạo thành ma trận R = (A|I)
5. Thực hiện phép biến đổi guass - jordan trên ma trận R
6. Kiểm tra R có dạng (I|B) không với I có kích thước n*n. 
    - Nếu có trả về ma trận B
    - Nếu không thì ma trận không khả nghịch, trả về 0
## 2. Cách chạy chương trình
- Cho người dùng nhập m,n tương ứng với số dòng,cột.
- Cho người dùng nhập từng phần tử cho từng dòng, xuất phát từ 0.
- Thực hiện hàm tìm ma trận nghịch đảo, gán vào biến B.
- Nếu B = 0 tức ma trận không khả nghịch, in lên màn hình. 
  Nếu B ra một ma trận tức đó là kết quả, in ra mà hình ma trận đó.
var firstDate = new Date();
firstDate.setDate(1); //第一天
var endDate = new Date(firstDate);
endDate.setMonth(firstDate.getMonth() + 1);
endDate.setDate(0);
alert(
  "第一天：" +
    new Date(firstDate).toString("yyyy-MM-dd") +
    " 最后一天：" +
    new Date(endDate).toString("yyyy-MM-dd")
);
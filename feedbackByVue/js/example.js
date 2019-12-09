var app = new Vue({
  el: "#todoapp",
  data: {
    list: ["test1", "test12", "test13"],
    inputValue: ""
    listTest:[
      
    ]
  },
  methods: {
    add: function () {
      this.list.push(this.inputValue);
    },
    remove: function (index) {
      console.log("删除");
      console.log(index);
      this.list.splice(index, 1);
    },
  },
})
$ui.render({
    views: [
      {
        type: "label",
        props: {
          bgcolor: $color("#000000")
        },
        layout: function(make, view) {
          make.center.equalTo(view.super)
          make.size.equalTo($size(50, 50))
        },
        events: {
          tapped: function(sender) {
  
          }
        }
      }
    ]
  })
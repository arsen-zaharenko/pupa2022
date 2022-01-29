function addInputTag(e) {
    let lastInput = $("form").children().last();
    let newInputId = parseInt(lastInput.attr("id")) + 1;
    let newInput = $("<input/>").attr("id", newInputId)
                                .attr("name", "input")
                                .attr("value", "input " + newInputId);
    lastInput.after(newInput).after("<br>");
}
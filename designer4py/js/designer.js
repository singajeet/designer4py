/*
 * Designer js file
 */
/*
$.getScript("https://ajax.googleapis.com/ajax/libs/prototype/1.7.3.0/prototype.js", function(){alert('prototype loaded');});
*/

var ToolNode = Class.create({
	id: "",
	toolName: "",
	type: "TOOL",
	shape: "square",
	bgColor: "grey",
	mode: "toolBox",
	nativeType: "node",
	initialize: function(id, toolName){
		this.id = id;
		this.toolName = toolName;
	},
	getData: function(){
		node = {};
		node['data'] = {};
		node['data']['id'] = this.id;
		node['data']['type'] = this.type;
		node['data']['toolName'] = this.toolName;
		return node;
	},
	getStyle: function(){
		nodeStyle = {};
		selector = "node[type='" + this.type + "']";
		style = {};
		style['shape'] = this.shape;
		style['background-color'] = this.bgColor;
		nodeStyle['selector'] = selector;
		nodeStyle['style'] = style;
		return nodeStyle;
	}
});

var DimTool = Class.create(ToolNode, {
		type: "DIM",
		shape: "triangle",
		bgColor: "blue"
	});

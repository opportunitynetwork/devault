var Environment = React.createClass({
render: function() {
  return (
    <tr>
      <td className="environmentName">{this.props.name}</td>
      <td className="environmentTier">{this.props.tier}</td>
      <td className="environmentVersion">{this.props.version}</td>
    </tr>
  );
}
});

var EnvironmentList = React.createClass({
render: function() {
	if (this.props.data.results)
	{
	    var environmentNodes = this.props.data.results.map(function(environment) {
    return (
      <Environment name={environment.name} tier={environment.tier} version={environment.current_version} 	key={environment.id}>
        {environment.name}
      </Environment>
    );
  });
	} else var environmentNodes = this.props.data.map(function(environment) {
    return (
      <Environment name={environment.name} 	key={environment.id}>
        {environment.name}
      </Environment>
    );
  });

  return (
    <table   className="environmentList" >
      <thead>
        <tr>
          <td >Name</td>
          <td >Tier</td>
          <td >Version</td>
        </tr>
      </thead>
      <tbody>
        {environmentNodes}
      </tbody>
    </table>
  );
}
});

var EnvironmentBox = React.createClass({
  getInitialState: function() {
  return {data: []};
},
loadEnvironmentsFromServer: function() {
  $.ajax({
    url: this.props.url,
    dataType: 'json',
    cache: false,
    success: function(data) {
      this.setState({data: data});
    }.bind(this),
    error: function(xhr, status, err) {
      console.error(this.props.url, status, err.toString());
    }.bind(this)
  });
},
getInitialState: function() {
  return {data: []};
},
componentDidMount: function() {
  this.loadEnvironmentsFromServer();
  setInterval(this.loadEnvironmentsFromServer, this.props.pollInterval);
},
render: function() {
  return (
    <div className="environmentBox">      
      <EnvironmentList data={this.state.data}/>
    </div>
  );
}
});
ReactDOM.render(
  <EnvironmentBox url="/environments/" pollInterval={2000} />,
  document.getElementById('content')
);
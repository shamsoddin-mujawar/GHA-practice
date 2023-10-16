const core = require('@actions/core');
const github = require('@actions/github');

function run(){
    try {
      // `name` input defined in action metadata file
      const i_name = core.getInput('name');
      console.log(`Hello ${i_name}!`);
      core.setOutput("user_name", i_name);
    } catch (error) {
      core.setFailed(error.message);
    }
}

run();

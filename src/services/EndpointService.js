export class EndpointService {
  async performBusinessLogic(data) {
    try {
      if (!data || typeof data !== 'object') {
        throw new Error('Invalid input data');
      }
      const result = await db.query(data);
      return result;
    } catch (error) {
      console.error(error);
      throw error;
    }
  }
}